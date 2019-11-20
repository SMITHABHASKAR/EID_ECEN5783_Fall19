# based on code by Lea Albaugh, who was a visiting researcher in the Unstable Design Lab during Summer 2019
# Thanks, Lea!

import math
import sys, os
import socket
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtNetwork import *

_TPM = 220 # 220 threads controlled by each module in the loom

# byte arrays
turnVacuumOff = bytes(b'\x01\x01\x01')
turnVacuumOn = bytes(b'\x01\x01\x04')
initiateLoomConnection = bytes(b'\x04\x0e')

def printOutput(output):
    print (output)

# this QThread represents the TCP connection to the loom
# job 1: keeping TCP socket alive (TODO?)
# job 2: handle incoming data from loom as they come in (with a simple socket, the LoomHandler had to call socket.recv everytime)
# job 3: handle things to be written to the loom when the Loom
class LoomControl(QObject):
    def __init__(self, loom, parent=None):
        super(LoomControl, self).__init__(parent)
        self.loom = loom

        self.qsocket = QTcpSocket(self)
        self.qsocket.setSocketOption(QAbstractSocket.KeepAliveOption, 1)

        self.address = None
        self.port = None

        self.qsocket.readyRead.connect(self.read)
        self.qsocket.stateChanged.connect(printOutput)
        self.qsocket.disconnected.connect(self.loom.loomDisconnected)
        
        #self.create_socket() # same options as socket.socket(opts)
        #self.set_reuse_addr()
        #self.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    def connect(self):
        #self.socket.connect((self.address, self.port))
        self.qsocket.connectToHost(self.address, self.port)
        if not self.loom.connected:
            self.loom.loomConnected.emit()
        self.loom.connected = True

    def send(self, data):
        print ("LoomControl: sending ", data)
        #self.socket.send(data)
        self.qsocket.write(data)
    
    def read(self):
        print ("data available to read")
        #data = self.socket.recv(1024)
        qdata = self.qsocket.readAll()
        if (qdata is not bytes()):
            self.loom.received = qdata
            #self.parent.messageFromLoom.emit()
            #print (data)
            print(qdata)
            self.loom.messageFromLoom.emit(str(qdata))
            print ("emitted messageFromLoom signal")

# make loom a QObject so that it can handle events in a GUI-friendly way
class Loom(QtCore.QObject): 
    # signals here
    loomConnectionChanged = QtCore.pyqtSignal(bool) # emitted when self.connected changes
    loomConnected = QtCore.pyqtSignal() # emitted when self.connected goes from False to True
    loomDisconnected = QtCore.pyqtSignal() # emitted when self.connected goes from True to False

    vacuumChanged = QtCore.pyqtSignal() # emitted when loom responds to vacuum command

    messageFromLoom = QtCore.pyqtSignal(str) # emitted when self.loomcontrol socket receives a message from the loom
    pickRequest = QtCore.pyqtSignal() # emitted when message from loom matches the format for a pick request
    
    # int array for lookup table (reordering bits for a loom pick)
    lookup = [7, 5, 3, 151, 149, 55, 53, 51, 199, 197, 1, 11, 9, 147, 145, 49, 59, 57, 195, 193, 23, 21, 155, 153, 71, 69, 67, 203, 201, 19, 17, 31, 167, 165, 65, 79, 77, 215, 213, 29, 27, 25, 163, 161, 75, 73, 87, 211, 209, 39, 37, 35, 175, 173, 85, 83, 81, 223, 221, 33, 47, 45, 171, 169, 95, 93, 219, 217, 43, 41, 6, 183, 181, 91, 89, 103, 231, 229, 4, 2, 0, 179, 177, 101, 99, 97, 227, 225, 10, 8, 22, 191, 189, 107, 105, 119, 239, 237, 20, 18, 16, 187, 185, 117, 115, 113, 235, 233, 30, 28, 150, 148, 127, 125, 123, 198, 196, 26, 24, 38, 146, 144, 121, 135, 133, 194, 192, 36, 34, 32, 154, 152, 131, 129, 143, 202, 200, 46, 44, 42, 166, 164, 141, 139, 137, 214, 212, 40, 54, 52, 162, 160, 102, 100, 210, 208, 50, 48, 58, 174, 172, 98, 96, 106, 222, 220, 56, 70, 68, 170, 168, 104, 118, 116, 218, 216, 66, 64, 78, 182, 180, 114, 112, 126, 230, 228, 76, 74, 72, 178, 176, 124, 122, 120, 226, 224, 86, 84, 190, 188, 134, 132, 130, 238, 236, 82, 80, 94, 186, 184, 128, 142, 140, 234, 232, 92, 90, 88, 138, 136]

    def __init__(self, numberOfModules, parent = None):
        super(Loom, self).__init__(parent)

        # tcp socket built into Python
        self.loomcontrol = LoomControl(self) #socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.loomcontrol.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.modules = numberOfModules
        self.threads = self.modules * _TPM
        self.pickNumber = 0 # the number of rows that have been sent to the loom
        self.vacuumOn = False
        self.connected = False

        self.received = None

        self.messageFromLoom.connect(self.isPickRequest)

        print("ready to connect")

    def connectLoom(self, address, port):
        # ip address = string, port = int
        self.loomcontrol.address = address
        self.loomcontrol.port = port
        print ("connecting to loom at ",address,":",port)
        if not (self.connected):
            try:
                self.loomcontrol.connect()
            except:
                print ("socket: connection failed")
        print ("sending connect packets to loom")
        self.loomcontrol.send(initiateLoomConnection)

        return self.connected

    def toggleVacuum(self):
        if self.vacuumOn:
            print ("sending vacuum off")
            self.loomcontrol.send(turnVacuumOff);
            self.vacuumOn = False
        else:
            print ("sending vacuum on")
            self.loomcontrol.send(turnVacuumOn);
            self.vacuumOn = True
    
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
            if (m%2 == 0): modAmount = 1

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

    def isPickRequest(self):
        #println(javax.xml.bind.DatatypeConverter.printHexBinary(data));
        print ("checking if received message is a pick request")
        if (len(self.received) == 11 and self.received[0] == b'\x05'):
            print("a request!")
            self.pickRequest.emit()
            return True
        elif (len(self.received) == 4 and self.received[2] == b'\x04'):
            print("received vacuum on confirmation")
            self.vacuumChanged.emit()
        else:
            print ("not a request")
            return False
