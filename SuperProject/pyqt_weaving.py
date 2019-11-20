# GUI portion: during weaving

# Details/state description: vacuum is on, threads are raised, weaver should have shuttles ready and does not have hands available except for simple button presses

import numpy as np
import cv2 as cv
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import *
from PyQt5.QtGui import *

sys.path.insert(1, './TCP') # Loom.py is in the TCP folder

from Loom import Loom
from minimalLoomConnection import * # use the functions already built in this file

# simple woven patterns for testing, store as a list of lists or AxB matrix
# for example, plainweave represents:   0   1 
#                                       1   0 
_TABBY = [[0, 1], [1, 0]]
_TWILL = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
_WAFFLE = [[0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0]]

patternOptions = [["Tabby",_TABBY], ["Twill",_TWILL], ["Waffle",_WAFFLE]]

# how to import pattern arrays from patterns.json?

# yarns listed as [ SHORTCODE, HEX_COLOR ]
yarn = [] # if yarn list is blank, fill with default yarn ['A', '0xFFFFFF'] (yarn A, white color)
twoYarns = [['A', '0xFFFFFF'], ['B', '0xFF0000']]

_ROWWIDTH = 1320
_BLOCKSIZE = 20

# diagnostic/debugging settings
realLoom = True # connect to a dummy TCP server
_MODULES = 6

# connection settings
_PORT = 62000
_IPADDRESS = '192.168.7.20'

# render pattern draft in QT for tracker
# from https://stackoverflow.com/questions/39614777/how-to-draw-a-proper-grid-on-pyqt
class patternDraft(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.squares = [] # elements in the scene
        self.pattern = []
        self.blockSize = 20
        self.patternHeight = 0
        self.patternWidth = 0

        # styles for rendering
        self.linePen = QPen(QColor(128, 128, 128), 3) # gray line w/ weight 4
        self.blackFill = QBrush(QColor(0, 0, 0))
        self.whiteFill = QBrush(QColor(255, 255, 255))
        
    def drawDraft(self, pattern):
        self.clear()
        self.pattern = pattern # 2D int array

        self.patternHeight = len(pattern)
        self.patternWidth = len(pattern[0])
        width = self.patternWidth * _BLOCKSIZE
        height = self.patternHeight * _BLOCKSIZE
        self.setSceneRect(0, 0, width, height)
        self.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        
        for row in range(0, len(self.pattern)):
            for cell in range(0, len(pattern[row])):
                xc = cell * _BLOCKSIZE
                yc = row * _BLOCKSIZE
                data = pattern[row][cell] # 0 or 1
                if data is 1:
                    fill = self.blackFill
                elif data is 0:
                    fill = self.whiteFill
                self.addRect(xc, yc, _BLOCKSIZE, _BLOCKSIZE, self.linePen, fill)
    
    def placeMarker(self, row):
        xm = 0
        ym = row * _BLOCKSIZE
        self.addRect(xm, ym, self.patternWidth + 10, _BLOCKSIZE)
    
    #   BUTTON: Pause

    #   DISPLAY: Row number

    #   DISPLAY: Pattern repeat tracker
    #   Function/Appearance:
    #   - shows drawdown for the woven structure
    #   - marker that shows place in the structure

    #   DISPLAY: Yarn for this row (solid color or short code)

    #   DISPLAY: Weaving Progress/History (similar to entrance menu's)
    #   Function/Appearance:
    #   - the current row being woven (highlighted/boxed?)
    #   - below the current row, the previous rows that had been woven this session (grayed out?)

    #   DISPLAY (or buttons?): pedals (reverse, refresh, advance)
    #   Function/Appearance:
    #   - ALL: highlight/change color when physical pedal pressed
    #   - Reverse: send loom the previously woven row
    #   - Refresh: send loom the current row again
    #   - Advance: send loom the next row in design

class Ui_Form(QtWidgets.QMainWindow):
  def setupUi(self, Form):
    Form.setObjectName("Loom")
    Form.resize(500,350)

    self.loomHandler = Loom(_MODULES)
    #self.loomControl = self.loomHandler.loomcontrol # a TCP socket

    self.connectButton = QtWidgets.QPushButton(Form)
    self.connectButton.setGeometry(QtCore.QRect(10, 10, 100, 40))
    self.connectButton.setObjectName("connect")

    self.terminal = QtWidgets.QTextEdit(Form)
    self.terminal.setGeometry(QtCore.QRect(270, 60, 210, 210))
    self.terminal.setObjectName("terminal")
    self.terminal.setReadOnly(True)

    self.draft = patternDraft()
    self.draftView = QtWidgets.QGraphicsView(self.draft, Form)
    self.draftView.setGeometry(QtCore.QRect(10, 70, 200, 200))
    self.draftView.setScene(self.draft)

    self.selectPattern = QtWidgets.QComboBox(Form)
    self.selectPattern.setGeometry(QtCore.QRect(10, 60, 200, 30))
    self.selectPattern.addItems(["Select pattern", "Tabby", "Twill", "Waffle"])
    
    # buttons available after connection established
    self.vacuum = QtWidgets.QPushButton(Form)
    self.vacuum.setGeometry(QtCore.QRect(120, 10, 100, 40))
    self.vacuum.setObjectName("vacuumToggle")
    self.vacuum.setEnabled(False)

    self.tabby = QtWidgets.QPushButton(Form)
    self.tabby.setGeometry(QtCore.QRect(230, 10, 100, 40))
    self.tabby.setObjectName("tabby")
    self.tabby.setEnabled(False)

    self.stop = QtWidgets.QPushButton(Form)
    self.stop.setGeometry(QtCore.QRect(340, 10, 100, 40))
    self.stop.setObjectName("stopButton")
    self.stop.setEnabled(False)
    self.stop.setVisible(False) # hidden until paused = true

    # emulate pedal with GUI button
    self.advance = QtWidgets.QPushButton(Form)
    self.advance.setGeometry(QtCore.QRect(290, 280, 60, 60))
    self.advance.setEnabled(False)
    self.advance.setVisible(False) # hidden until started = true

    # reverse pedal
    self.reverse = QtWidgets.QPushButton(Form)
    self.reverse.setGeometry(QtCore.QRect(150, 280, 60, 60))
    self.reverse.setVisible(False)

    # refresh pedal
    self.refresh = QtWidgets.QPushButton(Form)
    self.refresh.setGeometry(QtCore.QRect(220, 280, 60, 60))

    self.pedals = [self.advance, self.reverse, self.refresh]
    self.activeFunctions = [self.vacuum, self.tabby, self.stop] + self.pedals

    for button in self.activeFunctions:
        button.setEnabled(False)
    for pedal in self.pedals:
        pedal.setVisible(False)

    self.retranslateUi(Form)

    #button connections
    self.connectButton.clicked.connect(Form.connectLoom)
    self.vacuum.clicked.connect(Form.vacuum)
    self.tabby.clicked.connect(Form.updateLoomState)
    self.stop.clicked.connect(Form.stopLoom)
    self.advance.clicked.connect(Form.advance)
    self.selectPattern.currentIndexChanged.connect(Form.updatePatternSelected)

    #loom events
    self.loomHandler.messageFromLoom.connect(Form.logData)
    self.loomHandler.loomConnected.connect(Form.activateUI)
    self.loomHandler.loomDisconnected.connect(Form.deactivateUI)
    self.loomHandler.pickRequest.connect(Form.advance)
    self.loomHandler.vacuumChanged.connect(Form.sendToLoom)

    QtCore.QMetaObject.connectSlotsByName(Form)

  def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "Loom Connection"))
    self.connectButton.setText(_translate("Form", "Connect"))
    self.vacuum.setText(_translate("Form", "Vacuum Toggle"))
    self.tabby.setText(_translate("Form", "Start Tabby"))
    self.stop.setText(_translate("Form", "Stop"))
    self.advance.setText(_translate("Form", "Next"))
    self.reverse.setText(_translate("Form", "Back"))
    self.refresh.setText(_translate("Form", "Again"))

class Form(Ui_Form):
    def __init__ (self, parent = None):
        super(Form, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.patternSelected = _TWILL
        self.lineNumber = 0
        self.patternRow = 0
        self.rowBuffer = None # row buffer, holds data for current row in case of refresh

        self.loomConnected = False
        self.vacuumOn = False
        self.loomState = "stopped" # stopped, started, paused

        #self.ui.draft.drawDraft(self.patternSelected)

    def updatePatternSelected(self, pattern):
        print (pattern)
        if (pattern is 1):
            self.patternSelected = _TABBY
        elif (pattern is 2):
            self.patternSelected = _TWILL
        elif (pattern is 3):
            self.patternSelected = _WAFFLE
        
        self.ui.draftView.setScene(self.ui.draft)
        self.ui.draft.drawDraft(self.patternSelected)

    def connectLoom(self):
        # loom = Loom(false); 
        # second parameter is whether or not the loom is "real" -- 
        # use false for debugging (sending to the fake node loom; 
        # change to true to communicate with the actual loom
        if not realLoom:
          print ("connecting to fake loom")
          port = 1337
          ipAddress = '127.0.0.1'
        else:
          port = _PORT
          ipAddress = _IPADDRESS
          print ("connecting to real loom at ",ipAddress,":",port)
        print ("making connection request")
        result = self.ui.loomHandler.connectLoom(ipAddress, port)
        if (result):
          print ("GUI: connection successful")
        else:
          print ("GUI: connection failed")

    def vacuum(self):
        print ("sending vacuum toggle")
        self.ui.loomHandler.toggleVacuum()
        if (self.vacuumOn):
          self.vacuumOn = False
        elif not (self.vacuumOn):
          self.vacuumOn = True

    def logData(self, event):
        print ("logging received in terminal")
        newEntry = str(event)#self.ui.loomHandler.received)
        print ("got new entry from loomHandler")
        self.ui.terminal.append(newEntry)
        print ("appended to terminal")

    def activateUI(self):
        print ("connection successful! enabling functions")
        self.ui.connectButton.setEnabled(False)
        for function in self.ui.activeFunctions:
          function.setEnabled(True)

    def deactivateUI(self):
        print ("connection broken!!!")
        self.ui.connectButton.setEnabled(True)
        for function in self.ui.activeFunctions:
          function.setEnabled(False)

    def updateLoomState(self):
        if (self.loomState == "stopped" or self.loomState =="paused"): # transition from stopped to starting
            for pedal in self.ui.pedals:
                pedal.setVisible(True) # started weaving, pedal is available
                pedal.setEnabled(True)
            self.ui.stop.setVisible(False)
            self.loomState = "started"
            self.ui.tabby.setText("Pause")
            self.vacuum()
            self.advance() # weaver can step on the pedal, "next" button not necessary
          #time.sleep(2)
          #self.sendToLoom() # need to wait until vacuum on confirm
        elif (self.loomState == "started"): # transition from started to paused
            self.loomState = "paused"
            self.vacuum()
          # need to resend current pick here, did not advance
            self.ui.tabby.setText("Resume")
            for pedal in self.ui.pedals:
                pedal.setEnabled(False)
            self.ui.stop.setVisible(True)
  
    def stopLoom(self):
        self.loomState = "stopped"
        if (self.vacuumOn):
            self.vacuum()
        for pedal in self.ui.pedals:
            pedal.setVisible(False)
        self.ui.stop.setVisible(False)
        self.ui.tabby.setText("Start Tabby")

    def advance(self):
        #if (self.loomHandler.askingForPick):
          #print ("loom asking for pick")
        self.lineNumber += 1
        self.rowBuffer = self.renderNextPick()
        self.sendToLoom()

    def sendToLoom(self):
        if (self.rowBuffer is not None):
            self.ui.loomHandler.sendPick(self.rowBuffer)
            print ("sent pick " +str(self.lineNumber))

    def renderNextPick(self):
        self.ui.terminal.append("rendering pick " + str(self.lineNumber))
        #return self.tabby(1320, self.lineNumber)
        #return self.weavePattern(_TWILL)
        return self.weavePattern(self.patternSelected)

  # loom takes picks as a list of 1 or 0. The first number in the list is the leftmost warp.
  # returns: int array
    def tabby(self, threads, rowNumber):
        pattern = []
        for i in range(0, threads):
          thread = 1;
          if (i%2 == rowNumber%2): 
            thread = 0
          pattern.append(thread)
        return pattern

    # weaving other patterns
    # return a pick filled with the row of a pattern
    def patternToRow(self, pattern):
        fill = pattern[self.patternRow] # slice the pattern array
        rowToSend = np.append(fill, fill)
        while (rowToSend.size < _ROWWIDTH):
            rem = _ROWWIDTH - rowToSend.size
            if (rem < len(fill)):
                rowToSend = np.append(rowToSend, fill[0:rem])
            else:
                rowToSend = np.append(rowToSend, fill)

        # print(rowToSend)
        return rowToSend

    def weavePattern(self, patternArray):
        self.patternRow = self.lineNumber % len(patternArray)
        #rowToSend = self.patternArray[self.patternRow] # just print the unit
        rowToSend = self.patternToRow(patternArray)
        #self.totalRows += 1
        return rowToSend


# plainweaveRow = patternToRow(plainweave)
#twillRow = patternToRow(twill)
#print (plainweaveRow.size)
#print (twillRow.size)

#weaver = weavingTracker()
#for i in range(0, 10):
#    weaving = weaver.weavePattern(_TWILL)
#    print (weaving)

# MAIN
if __name__ == "__main__":
  # how to make Python put out more useful info when crashing
  # from: https://www.reddit.com/r/learnpython/comments/7or35q/questionpyqt5threading_my_gui_crash_whit_no_error/
    sys._excepthook = sys.excepthook 
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback) 
        sys.exit(1) 
    sys.excepthook = exception_hook 

    class AppWindow(QtWidgets.QDialog):
        def __init__(self): 
            super().__init__()
            self.ui = Ui_Form() 
            self.ui.setupUi(self)
            self.show()

    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    app.exec_()
