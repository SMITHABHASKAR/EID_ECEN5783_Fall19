import math
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QByteArray

_TPM = 220 # 220 threads controlled by each module in the loom

# byte arrays
turnVacuumOff = QByteArray(bytearray(b'\x01\x01\x01'))
turnVacuumOn = QByteArray(bytearray(b'\x01\x01\x04'))
initiateLoomConnection = QByteArray(bytearray(b'\x04\x0e'))

def printOutput(output):
    print (output)

class LoomControl(QtNetwork.QTcpSocket):
    # see documentation https://doc.qt.io/qtforpython/PySide2/QtNetwork/QTcpSocket.html

    loomConnect = QtCore.pyqtSignal(int)
    received = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(LoomControl, self).__init__(parent)

    # def connect(self, address, port):
    # 	# ip address = string, port = int
    # 	super(LoomControl).connectToHost(self, address, port

class Loom(object): 
    # self.loomcontrol = LoomControl() # using QT equiv of a network client, send/receive QByteArrays
    # QByteArray documentation: https://doc.qt.io/qtforpython/PySide2/QtCore/QByteArray.html
    
    # int array for lookup table (reordering bits for a loom pick)
    lookup = [7, 5, 3, 151, 149, 55, 53, 51, 199, 197, 1, 11, 9, 147, 145, 49, 59, 57, 195, 193, 23, 21, 155, 153, 71, 69, 67, 203, 201, 19, 17, 31, 167, 165, 65, 79, 77, 215, 213, 29, 27, 25, 163, 161, 75, 73, 87, 211, 209, 39, 37, 35, 175, 173, 85, 83, 81, 223, 221, 33, 47, 45, 171, 169, 95, 93, 219, 217, 43, 41, 6, 183, 181, 91, 89, 103, 231, 229, 4, 2, 0, 179, 177, 101, 99, 97, 227, 225, 10, 8, 22, 191, 189, 107, 105, 119, 239, 237, 20, 18, 16, 187, 185, 117, 115, 113, 235, 233, 30, 28, 150, 148, 127, 125, 123, 198, 196, 26, 24, 38, 146, 144, 121, 135, 133, 194, 192, 36, 34, 32, 154, 152, 131, 129, 143, 202, 200, 46, 44, 42, 166, 164, 141, 139, 137, 214, 212, 40, 54, 52, 162, 160, 102, 100, 210, 208, 50, 48, 58, 174, 172, 98, 96, 106, 222, 220, 56, 70, 68, 170, 168, 104, 118, 116, 218, 216, 66, 64, 78, 182, 180, 114, 112, 126, 230, 228, 76, 74, 72, 178, 176, 124, 122, 120, 226, 224, 86, 84, 190, 188, 134, 132, 130, 238, 236, 82, 80, 94, 186, 184, 128, 142, 140, 234, 232, 92, 90, 88, 138, 136]

    def __init__(self, loomControl, numberOfModules, parent = None):
        self.loomcontrol = QtNetwork.QTcpSocket()
        self.modules = numberOfModules
        self.threads = self.modules * _TPM
        self.pickNumber = 0 # the number of rows that have been sent to the loom
        self.vacuumOn = False

        #self.loomcontrol.error.connect(self.loomcontrol.error)
        self.loomcontrol.stateChanged.connect(printOutput)
        self.loomcontrol.hostFound.connect(printOutput)
        self.loomcontrol.readyRead.connect(printOutput)

        print("ready to connect")

    def readMessage(self):
        print ("reading available data")
        received = self.loomcontrol.readAll() # returns QByteArray
        print (received)
        return QtCore.QString(received)

    def connectLoom(self, address, port):
    	# ip address = string, port = int
        print ("connecting to loom at ",address,":",port)
        try:
            self.loomcontrol.connectToHost(address, port)
        except connectionFailure:
            print ("connection failed")
        #print ("sending connect packets to loom")
        #self.loomcontrol.write(initiateLoomConnection)
        # todo: write loom connected event, received loom ACK signal

    def toggleVacuum(self):
        if self.vacuumOn:
            self.loomcontrol.write(turnVacuumOff);
            self.vacuumOn = False
        else:
            self.loomcontrol.write(turnVacuumOn);
            self.vacuumOn = True
    
    # input: pick is an int[]
    # return: none
    def sendPick(self, pick):
        # add mystery data and picknumber data
        frontMatter = QByteArray({0x05, 0x02, chr(pickNumber%255), 0x00, 0x06, 0x01, 0x06})

        # turn on the vacuum if necessary
        if not self.vacuumOn: self.toggleVacuum()

        # write that pick data as a byte array (QByteArray)
        toSend = frontMatter.append(pickToBytes(pick))
        #print "We say: "
        #print toSend
        self.loomcontrol.write(toSend)
        self.pickNumber += 1

        # inputs: int[] pick
        # returns: QByteArray
        def pickToBytes(self, pick):
            moduleOrder = [1, 4, 2, 5, 3, 6]
            packedBytes = QByteArray()

            # slicing and dicing here
            # for (int i=1; i<=modules; i++) {
            for m in moduleOrder:
                i = moduleOrder[m]
                # add the name of the module
                packedBytes.append(chr(i))

                # initialize a module
                # int bitsInModule = tpm; 
                # if (tpm%8 != 0) bitsInModule = tpm  + (8 - tpm%8); # round up to a multiple of 8
                bitsInModule = 240 # actually let's try the full 240 that it seems to want
                #println("bitsinmodule: "+bitsInModule);
                module = [] # according to the internet, default value of int is 0, so let's fill with 1

                for b in range(0, len(module)):
                    module[b] = 1

                    # fill in the module
                    modAmount = 0 # the first half of the modules handle the evens; the second half handle the odds
                    # this is specific to a 2-deep module config
                    if (i <= modules/2):
                        modAmount = 1

                    #int index=0;
                    # t is a thread in the pick. Let's look at just this module. We'll start by breaking the full pick into thirds...
                    rightedge = self.threads - (((i-1)%(self.modules/2)) * (_TPM*2)) - 1
                    leftedge = rightedge - (_TPM*2) + 1
                    #println("module "+i+", leftedge: "+leftedge+", rightedge: "+rightedge);
                    for t in range(rightedge, leftedge, -1): # by going from right to left, we're shuffling the order so the input pick can be left to right
                        if (t%2 == modAmount): # ...then just look at the evens/odds (whichever this module handles)
                            threadLocationInModule = math.floor((rightedge - t)/2)
                            module[lookup[threadLocationInModule]] = pick[t]
                        #index++;

            # we no longer do this trick, since, with the lookup table approach, the data gaps simply don't get filled in.
            # leaving this here anyway as a record of where the gaps are
            #if (index == 12 || index == 60 || index == 108 || index == 156 || index == 204) { # this is where the gaps in the data are -- fill with '1's
            #  for (int j = 0; j<4; j++) {
            #    module[index] = 1;
            #    index++;
            #  }
            #}

            # pack those bits into bytes
            for numByte in range(0, len(module)/8):
                j = numByte*8
                thisByte = chr( module[j]<<7 | module[j+1]<<6 | module[j+2]<<5 | module[j+3]<<4 | module[j+4]<<3 | module[j+5]<<2 | module[j+6]<<1 | module[j+7]<<0 ); 
                packedBytes.append(thisByte)

            #then turn it into a proper array
            # bytesPick = new byte[packedBytes.size()]; 
            # for (int i = 0; i < packedBytes.size(); i++) {
            #   byte thisByte = packedBytes.get(i); 
            #   bytesPick[i] = thisByte;

            return packedBytes # bytesPick

        def isPickRequest(self, data):
            #println(javax.xml.bind.DatatypeConverter.printHexBinary(data));
            if (data.length == 11 and data[0] == 0x05):
                print("a request!")
                return true
            else: 
                return false
