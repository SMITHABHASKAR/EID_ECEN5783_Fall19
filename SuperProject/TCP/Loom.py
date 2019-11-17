# based on code by Lea Albaugh, who was a visiting researcher in the Unstable Design Lab during Summer 2019
# Thanks, Lea!

import math
import sys, os
import socket
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QByteArray

_TPM = 220 # 220 threads controlled by each module in the loom

# byte arrays
turnVacuumOff = bytes(b'\x01\x01\x01')
turnVacuumOn = bytes(b'\x01\x01\x04')
initiateLoomConnection = bytes(b'\x04\x0e')

def printOutput(output):
    print (output)

class LoomControl(socket.socket):
    # see documentation https://doc.qt.io/qtforpython/PySide2/QtNetwork/QTcpSocket.html
    # QByteArray documentation: https://doc.qt.io/qtforpython/PySide2/QtCore/QByteArray.html

    def __init__(self, parent=None):
        super(LoomControl, self).__init__(parent)

    # def connect(self, address, port):
    #   # ip address = string, port = int
    #   super(LoomControl).connectToHost(self, address, port

# make loom a QObject so that it can handle events in a GUI-friendly way
class Loom(QtCore.QObject): 
    # signals here
    loomConnectionChanged = QtCore.pyqtSignal(bool) # emitted when self.connected changes
    loomConnected = QtCore.pyqtSignal() # emitted when self.connected goes from False to True
    loomDisconnected = QtCore.pyqtSignal() # emitted when self.connected goes from True to False

    vacuumChanged = QtCore.pyqtSignal(bool) # emitted when self.vacuum changes

    messageFromLoom = QtCore.pyqtSignal() # emitted when self.loomcontrol socket receives a message from the loom
    
    # int array for lookup table (reordering bits for a loom pick)
    lookup = [7, 5, 3, 151, 149, 55, 53, 51, 199, 197, 1, 11, 9, 147, 145, 49, 59, 57, 195, 193, 23, 21, 155, 153, 71, 69, 67, 203, 201, 19, 17, 31, 167, 165, 65, 79, 77, 215, 213, 29, 27, 25, 163, 161, 75, 73, 87, 211, 209, 39, 37, 35, 175, 173, 85, 83, 81, 223, 221, 33, 47, 45, 171, 169, 95, 93, 219, 217, 43, 41, 6, 183, 181, 91, 89, 103, 231, 229, 4, 2, 0, 179, 177, 101, 99, 97, 227, 225, 10, 8, 22, 191, 189, 107, 105, 119, 239, 237, 20, 18, 16, 187, 185, 117, 115, 113, 235, 233, 30, 28, 150, 148, 127, 125, 123, 198, 196, 26, 24, 38, 146, 144, 121, 135, 133, 194, 192, 36, 34, 32, 154, 152, 131, 129, 143, 202, 200, 46, 44, 42, 166, 164, 141, 139, 137, 214, 212, 40, 54, 52, 162, 160, 102, 100, 210, 208, 50, 48, 58, 174, 172, 98, 96, 106, 222, 220, 56, 70, 68, 170, 168, 104, 118, 116, 218, 216, 66, 64, 78, 182, 180, 114, 112, 126, 230, 228, 76, 74, 72, 178, 176, 124, 122, 120, 226, 224, 86, 84, 190, 188, 134, 132, 130, 238, 236, 82, 80, 94, 186, 184, 128, 142, 140, 234, 232, 92, 90, 88, 138, 136]

    def __init__(self, numberOfModules, parent = None):
        super(Loom, self).__init__(parent)

        # tcp socket built into Python
        self.loomcontrol = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.loomcontrol.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.modules = numberOfModules
        self.threads = self.modules * _TPM
        self.pickNumber = 0 # the number of rows that have been sent to the loom
        self.vacuumOn = False
        self.connected = False
        self.received = ""

        #self.loomcontrol.error.connect(self.loomcontrol.error)
        #self.loomcontrol.stateChanged.connect(printOutput)
        #self.loomcontrol.hostFound.connect(printOutput)
        #self.loomcontrol.readyRead.connect(printOutput)

        print("ready to connect")

    def readMessage(self):
        print ("reading available data")
        self.received = self.loomcontrol.recv(1024) # returns bytes
        print ("received", self.received)
        self.messageFromLoom.emit()
        print ("emitted messageFromLoom signal")
        # return QtCore.QString(received)

    def connectLoom(self, address, port):
        # ip address = string, port = int
        print ("connecting to loom at ",address,":",port)
        #try:
        self.loomcontrol.connect((address, port))
        # except:
        #   print ("socket: connection failed")
        print ("sending connect packets to loom")
        self.loomConnected.emit()
        self.loomcontrol.send(initiateLoomConnection)
        print ("initial send succeeded")
        try:
            print ("listening for response")
            self.readMessage()
        except:
            print ("initial send failed")
        else:
            print ("returning data to GUI")
        # todo: write loom connected event, received loom ACK signal

    def toggleVacuum(self):
        if self.vacuumOn:
            print ("sending vacuum off")
            self.loomcontrol.send(turnVacuumOff);
            self.vacuumOn = False
        else:
            print ("sending vacuum on")
            self.loomcontrol.send(turnVacuumOn);
            self.vacuumOn = True
        self.readMessage()
    
    # input: pick is an int[]
    # return: none
    def sendPick(self, pick):
        # add mystery data and picknumber data
        frontMatter = bytearray(b'\x05\x02') + bytes([self.pickNumber%255]) + bytearray(b'\x00\x06\x01\x06')

        # turn on the vacuum if necessary
        if not self.vacuumOn: self.toggleVacuum()
                
        # write that pick data as a byte array (Python bytes)
        toSend = frontMatter + self.pickToBytes(pick)
        #print "We say: "
        #print toSend
        self.loomcontrol.send(toSend)
        self.pickNumber += 1
        self.readMessage()

    # inputs: int[] pick
    # returns: bytes
    # ----------------------------------------
    def pickToBytes(self, pick):
        moduleOrder = [1, 4, 2, 5, 3, 6]
        packedBytes = bytes()

        # slicing and dicing here
        # for (int i=1; i<=modules; i++) {
        for m in range(0, 6):
            i = moduleOrder[m]
            # add the name of the module
            packedBytes += bytes([i])

            # initialize a module
            # int bitsInModule = tpm; 
            # if (tpm%8 != 0) bitsInModule = tpm  + (8 - tpm%8); # round up to a multiple of 8
            bitsInModule = 240 # actually let's try the full 240 that it seems to want
            #println("bitsinmodule: "+bitsInModule);
            module = [1] * bitsInModule # according to the internet, default value of int is 0, so let's fill with 1

            for b in range(0, len(module)):
                module[b] = 1

                # fill in the module
                modAmount = 0 # the first half of the modules handle the evens; the second half handle the odds
                # this is specific to a 2-deep module config
                if (m%2 == 0):
                    modAmount = 1

                #int index=0;
                # t is a thread in the pick. Let's look at just this module. We'll start by breaking the full pick into thirds...
                rightedge = int(self.threads - (((i-1)%(self.modules/2)) * (_TPM*2)) - 1)
                leftedge = rightedge - (_TPM*2) + 1
                #println("module "+i+", leftedge: "+leftedge+", rightedge: "+rightedge);
                for t in range(rightedge, leftedge, -1): # by going from right to left, we're shuffling the order so the input pick can be left to right
                    if (t%2 == modAmount): # ...then just look at the evens/odds (whichever this module handles)
                        threadLocationInModule = math.floor((rightedge - t)/2)
                        module[self.lookup[threadLocationInModule]] = pick[t]
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
                for numByte in range(0, int(len(module)/8)):
                    j = numByte*8
                    thisByte = module[j]<<7 | module[j+1]<<6 | module[j+2]<<5 | module[j+3]<<4 | module[j+4]<<3 | module[j+5]<<2 | module[j+6]<<1 | module[j+7]<<0
                    packedBytes += bytes([thisByte])

                #then turn it into a proper array
                # bytesPick = new byte[packedBytes.size()]; 
                # for (int i = 0; i < packedBytes.size(); i++) {
                #   byte thisByte = packedBytes.get(i); 
                #   bytesPick[i] = thisByte;

                return packedBytes # bytesPick
            # end pickToBytes --------------------------

        

        def isPickRequest(self, data):
            #println(javax.xml.bind.DatatypeConverter.printHexBinary(data));
            if (data.length == 11 and data[0] == 0x05):
                print("a request!")
                return true
            else: 
                return false
