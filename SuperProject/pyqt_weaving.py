# GUI portion: during weaving

# Details/state description: vacuum is on, threads are raised, weaver should have shuttles ready and does not have hands available except for simple button presses

import numpy as np
import cv2 as cv
import sys
import json
import qimage2ndarray as imgarr
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from weavingWidgets import * # patternDraft, custom dialogs
from designFileEditing import *
from pedalGPIO import * #pedalHandler

sys.path.insert(1, './TCP') # Loom.py is in the TCP folder
sys.path.insert(1, './testFiles') # access test images

from Loom import Loom

# simple woven patterns for testing, store as a list of lists or AxB matrix
# for example, plainweave represents:   0   1 
#                                       1   0 
#_TABBY = [[0, 1], [1, 0]]
#_TWILL = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
#_DOUBLE = [[0, 0, 0, 1], [0, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 1]]
#_WAFFLE = [[0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0]]
_ALLUP = [[1, 1, 1, 1]]

#_patternOptions = [Pattern("Tabby",_TABBY), Pattern("Twill",_TWILL), Pattern("Doubleweave", _DOUBLE), Pattern("Waffle",_WAFFLE), Pattern("All Up x 4", _ALLUP)]
_patternOptions = [Pattern("All Up x 4", _ALLUP)]

# yarns listed as [ SHORTCODE, HEX_COLOR ]
yarn = [] # if yarn list is blank, fill with default yarn ['A', '0xFFFFFF'] (yarn A, white color)
twoYarns = [['A', '0xFFFFFF'], ['B', '0xFF0000']]

_ROWWIDTH = 1320
_BLOCKSIZE = 20

# diagnostic/debugging settings
terminalHidden = True
realLoom = True # connect to a dummy TCP server if False
_MODULES = 6

# connection settings
_PORT = 62000
_IPADDRESS = '192.168.7.20'
    
    #   BUTTON: Pause

    #   DISPLAY: Row number

    #   DISPLAY: Yarn for this row (solid color or short code)

    #   DISPLAY (or buttons?): pedals (reverse, refresh, advance)
    #   Function/Appearance:
    #   - ALL: highlight/change color when physical pedal pressed
    #   - Reverse: send loom the previously woven row
    #   - Refresh: send loom the current row again
    #   - Advance: send loom the next row in design

class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Loom")
        Form.resize(800, 480)

        self.loomHandler = Loom(_MODULES)
        self.pedalHandler = pedalHandler()

        self.connectButton = QtWidgets.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(10, 10, 100, 40))
        self.connectButton.setObjectName("connect")
        self.connectButton.clicked.connect(Form.connectLoom)

        # display widgets: terminal, draft view, overall project view

        self.draft = patternDraft()
        self.draftView = QtWidgets.QGraphicsView(self.draft, Form)
        self.draftView.setGeometry(QtCore.QRect(10, 70, 200, 200))
        self.draftView.setScene(self.draft)

        self.project = projectProgress()
        self.projectView = QtWidgets.QGraphicsView(Form)
        self.projectView.setGeometry(QtCore.QRect(220, 60, 550, 210))
        self.projectView.setScene(self.project)
#        self.projViewLabel = QtWidgets.QLabel(self.projectView)
#        self.projViewLabel.setGeometry(QtCore.QRect(0, 0, 550, 210))

        self.terminal = QtWidgets.QTextEdit(Form)
        self.terminal.setGeometry(QtCore.QRect(270, 60, 210, 210))
        self.terminal.setObjectName("terminal")
        self.terminal.setReadOnly(True)
        if (terminalHidden):
            self.terminal.setVisible(False)

        # editing functions

        self.selectPattern = QtWidgets.QComboBox(Form)
        self.selectPattern.setGeometry(QtCore.QRect(10, 60, 200, 30))
        self.selectPattern.addItem("Select pattern")
        self.selectPattern.currentIndexChanged.connect(Form.updatePatternSelected)

        self.openFile = QtWidgets.QPushButton(Form)
        self.openFile.setGeometry(QtCore.QRect(9, 268, 202, 30))
        self.openFile.clicked.connect(Form.loadWeaveFile)
        
        # buttons available after connection established
        self.vacuum = QtWidgets.QPushButton(Form)
        self.vacuum.setGeometry(QtCore.QRect(120, 10, 100, 40))
        self.vacuum.setObjectName("vacuumToggle")
        self.vacuum.clicked.connect(Form.vacuum)

        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(230, 10, 100, 40))
        self.start.setObjectName("startButton")
        self.start.clicked.connect(Form.updateLoomState)

        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(340, 10, 100, 40))
        self.stop.setObjectName("stopButton")
        self.stop.setVisible(False) # hidden until paused = true
        self.stop.clicked.connect(Form.stopLoom)

        # advance pedal
        self.advance = QtWidgets.QPushButton(Form)
        self.advance.setGeometry(QtCore.QRect(440, 280, 60, 60))
        #self.advance.clicked.connect(Form.advance)

        # reverse pedal
        self.reverse = QtWidgets.QPushButton(Form)
        self.reverse.setGeometry(QtCore.QRect(300, 280, 60, 60))
        #self.reverse.clicked.connect(Form.reverse) # what should this do if user presses on-screen button instead of the pedal?

        # refresh pedal
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(370, 280, 60, 60))
        #self.refresh.clicked.connect(Form.sendToLoom) # change this so it won't collide with pedals

        self.pedals = [self.advance, self.reverse, self.refresh]
        self.activeFunctions = [self.vacuum, self.start, self.stop] + self.pedals
        self.editFunctions = [self.selectPattern]

        for button in self.activeFunctions: # enabled when loom connected
            button.setEnabled(False)
        for pedal in self.pedals: # hidden until loom state = started weaving
            pedal.setVisible(False)

        #loom events
        self.loomHandler.messageFromLoom.connect(Form.logData)
        self.loomHandler.loomConnected.connect(Form.activateUI)
        self.loomHandler.loomDisconnected.connect(Form.deactivateUI)
        self.loomHandler.pickRequest.connect(Form.sendToLoom)
        self.loomHandler.vacuumChanged.connect(Form.sendToLoom)

        # pedal events
        self.pedalHandler.advancePedalEvent.connect(Form.advance)
        self.pedalHandler.refreshPedalEvent.connect(Form.refresh)
        self.pedalHandler.reversePedalEvent.connect(Form.reverse)
        #self.pedalHandler.loomRelayEvent.connect(Form.pedalStep)

        QtCore.QMetaObject.connectSlotsByName(Form)
        self.retranslateUi(Form)

    def loadFileView(self):
        self.draftView.setVisible(False)
        self.projectView.setGeometry(QtCore.QRect(10, 60, 770, 210))
#        self.projViewLabel.setGeometry(QtCore.QRect(0, 0, 770, 210))

    def generateFileView(self):
        self.draftView.setVisible(True)
        self.projectView.setGeometry(QtCore.QRect(220, 60, 550, 210))
#        self.projViewLabel.setGeometry(QtCore.QRect(0, 0, 550, 210))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Loom Connection"))
        self.connectButton.setText(_translate("Form", "Connect"))
        self.vacuum.setText(_translate("Form", "Vacuum Toggle"))
        self.start.setText(_translate("Form", "Start"))
        self.stop.setText(_translate("Form", "Stop"))
        self.advance.setText(_translate("Form", "Next"))
        self.reverse.setText(_translate("Form", "Back"))
        self.refresh.setText(_translate("Form", "Again"))
        self.openFile.setText(_translate("Form", "Load file"))

class Form(Ui_Form):
    def __init__ (self, parent = None):
        super(Form, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.patternSelected = None
        self.lineNumber = -1
        self.patternRow = 0
        self.rowBuffer = None # row buffer, holds data for current row in case of refresh

        self.logging = True # if true, add rows to the image file being built
        self.weavingLog = np.empty((0,_ROWWIDTH))
        self.logPixmap = None
        self.weaveFile = None
        self.weaveBmp = None
        self.designMode = "generate" # generate OR load

        self.loomConnected = False
        self.vacuumOn = False
        self.loomState = "stopped" # stopped, started, paused
        self.pedalState = "ready" # "ready" to accept pedal press ("advance", "reverse", "refresh")

        self.connectLoom()
        self.loadPatternFile()

    def switchDesignMode(self):
        # switching to weaving from file
        if (self.designMode == "generate"):
            self.designMode = "load"
            self.ui.loadFileView()
        # switching to generating file
        elif (self.designMode == "load"):
            self.designMode = "generate"
            self.ui.generateFileView()
        else:
            self.logMessage("invalid mode")

    # import pattern arrays from patterns.json
    def loadPatternFile(self):
        # read JSON file and parse
        with open('patterns.json', 'r') as patternFile:
            data = patternFile.read() 
            self.patternList = json.loads(data) # a list of dicts

        for pattern in self.patternList:
        #    print ("pattern name: " + str(pattern['name']))
            self.ui.selectPattern.addItem(pattern['name'])
        #    print ("pattern data: " + str(pattern['pattern']))
        for pattern in _patternOptions:
            self.patternList.append(pattern)
            self.ui.selectPattern.addItem(pattern.name)

    def loadWeaveFile(self):
        # open QFileDialog
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Image files (*.bmp *.tif)")
        print (file) # tuple ('file path', 'ext')
        if (file[0] is not ''):
            print ("user loaded file")
            # load into QPixmap for display
            self.weaveFile = QPixmap(file[0])
#            self.weaveFile.setDevicePixelRatio(0.5)
            pixmapItem = self.ui.project.addPixmap(self.weaveFile)
            pixmapItem.setScale(2)
            self.ui.project.setDesign(self.weaveFile)
            # load BMP into cv for a numpy array
            self.weaveImg = cv.imread(file[0], cv.IMREAD_GRAYSCALE)
            if (self.designMode == "generate"):
                self.switchDesignMode()
        else: print ("user cancelled")

    def updatePatternSelected(self, pattern):
        selection = self.patternList[pattern-1]
        if (isinstance(selection, dict)):
            self.patternSelected = selection['pattern']#_patternOptions[pattern-1][1]
        else: # is Pattern object
            self.patternSelected = selection.data
        
        self.ui.draftView.setScene(self.ui.draft)
        self.ui.draft.drawDraft(self.patternSelected, True)
        if (self.designMode == "load"):
            self.switchDesignMode()

    def connectLoom(self):
        # whether or not the loom is "real" -- 
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

    def logMessage(self, message):
        print ("logging message in terminal")
        self.ui.terminal.append(message)

    def logData(self, event):
        print ("logging received in terminal")
        newEntry = str(event)
        print ("got new entry from loomHandler")
        self.ui.terminal.append(newEntry)
        print ("appended to terminal")

#   DISPLAY: Weaving Progress/History (similar to entrance menu's)
#   Function/Appearance:
#   - the current row being woven (highlighted/boxed?)
#   - below the current row, the previous rows that had been woven this session (grayed out?)

    def updateWeavingLog(self):
        if (self.designMode == "generate"):
            img = imgarr.array2qimage(self.weavingLog) # a QtGui.QImage
            pixmap = QtGui.QPixmap(img)
            pixmap.setDevicePixelRatio(0.5) # set pixmap ratio = half of real image -> pixmap pixels are magnified 2x
            #self.ui.project.clear()
            if (self.logPixmap is None):
                self.logPixmap = self.ui.project.addPixmap(pixmap)        
            else:
                self.logPixmap.setPixmap(pixmap)
        elif (self.designMode == "load"):
            print ("advance progress marker")

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
          
    def enableEdit(self):
        for function in self.ui.editFunctions:
            function.setEnabled(True)

    def disableEdit(self):
        for function in self.ui.editFunctions:
            function.setEnabled(False)

    def updateLoomState(self):
        if (self.loomState == "stopped" or self.loomState =="paused"): # transition from stopped to starting
            if (self.patternSelected is not None or self.weaveFile is not None):
                for pedal in self.ui.pedals:
                    pedal.setVisible(True) # started weaving, pedal is available
                    pedal.setEnabled(True)
                self.ui.stop.setVisible(False)
                for function in self.ui.editFunctions:
                    function.setEnabled(False)
                self.loomState = "started"
                self.ui.start.setText("Pause")
                self.vacuum()
                if (self.rowBuffer is None):
                    self.advance()
                else:
                    self.sendToLoom(False) # weaver can step on the pedal, "next" button not necessary
          #self.sendToLoom() # need to wait until vacuum on confirm
        elif (self.loomState == "started"): # transition from started to paused
            self.loomState = "paused"
            self.vacuum()
          # need to resend current pick here, did not advance
            self.ui.start.setText("Resume")
            for pedal in self.ui.pedals:
                pedal.setEnabled(False)
            for function in self.ui.editFunctions:
                function.setEnabled(True)
            self.ui.stop.setVisible(True)
  
    def stopLoom(self):
        self.loomState = "stopped"
        self.lineNumber = 0 # reset progress
        if (self.vacuumOn):
            self.vacuum()
        for pedal in self.ui.pedals:
            pedal.setVisible(False)
        self.ui.stop.setVisible(False)
        self.ui.start.setText("Start")
        # for now, also saves the weaving log image
        #if (self.logging):
        #    cv.imwrite('testWeavingLog.bmp', self.weavingLog)
        saveFile, ok = saveDialog.getSaveResult()
        print (saveFile, ok)

    def advance(self):
        if (self.pedalState == "ready"):
            self.pedalState = "advance" # pedal state reset after loom sends "ready" signal
            print ("GUI: advance pedal pressed")
            self.ui.advance.setDown(True)
        else:
            print ("GUI: not ready for pedal")

    def reverse(self):
        if (self.pedalState == "ready"):
            self.pedalState = "reverse" 
            print ("GUI: reverse pedal pressed")
            self.ui.reverse.setDown(True)
        else:
            print ("GUI: not ready for pedal")

    def refresh(self):
        if (self.pedalState == "ready"):
            self.pedalState = "refresh"
            print ("GUI: refresh pedal pressed")
            self.ui.refresh.setDown(True)
        else:
            print ("GUI: not ready for pedal")
        
    def sendToLoom(self, copy=True):
        if (self.pedalState == "advance"):
            self.lineNumber += 1
            self.rowBuffer = self.renderNextPick()
            self.ui.advance.setDown(False)
        elif (self.pedalState == "reverse"):                
            self.lineNumber -= 1
            self.rowBuffer = self.renderNextPick()
            self.ui.reverse.setDown(False)
        elif (self.pedalState == "refresh"):
            self.ui.refresh.setDown(False)
        else:
            print ("not a pedal press???")
            return
            
        if (self.rowBuffer is not None):
            self.ui.loomHandler.sendPick(self.rowBuffer)
            print ("sent pick " +str(self.lineNumber))
        # TODO: also send a copy of the rowBuffer to AWS or local server
            if (self.logging and copy):
                # sending to volatile array which is saved locally to .bmp
                pixelRow = self.rowToPixels(self.rowBuffer)
                self.weavingLog = np.insert(self.weavingLog, 0, [pixelRow], axis=0)
                self.updateWeavingLog()
                #print (self.weavingLog)
        if (self.designMode == "generate"):
            self.ui.draft.placeMarker(self.patternRow)
        self.ui.project.placeMarker(self.lineNumber)

        self.pedalState = "ready" # reset to wait for next press

    def renderNextPick(self):
        self.ui.terminal.append("rendering pick " + str(self.lineNumber))
        #return self.tabby(1320, self.lineNumber)
        #return self.weavePattern(_TWILL)
        if (self.designMode == "generate"):
            return self.weavePattern(self.patternSelected)
        elif (self.designMode == "load"):
            return self.rowFromImage(self.lineNumber)

    # loom takes picks as a list of 1 or 0. The first number in the list is the leftmost warp.
    # returns: int array
    # SAME AS self.weavePattern(_TABBY)
    def tabby(self, threads, rowNumber):
        pattern = []
        for i in range(0, threads):
          thread = 1;
          if (i%2 == rowNumber%2): 
            thread = 0
          pattern.append(thread)
        return pattern

    # weaving the selected pattern
    # return a pick filled with the row of a pattern
    def patternToRow(self, pattern):
        fill = pattern[self.patternRow] # slice the pattern array
        #for i in range(0, len(fill)):
        #    if fill[i] is True:
        #        fill[i] = 1
        #    elif fill[i] is False:
        #        fill[i] = 0
        print ("pattern row:", fill)
        rowToSend = np.append(fill, fill)
        while (rowToSend.size < _ROWWIDTH):
            rem = _ROWWIDTH - rowToSend.size
            if (rem < len(fill)):
                rowToSend = np.append(rowToSend, fill[0:rem])
            else:
                rowToSend = np.append(rowToSend, fill)
        # print(rowToSend)
        return rowToSend

    def rowToPixels(self, row):
        # rows sent to loom are 0's and 1's,
        # but a B&W bitmap needs 0 -> 255 for white pixels
        # and 1 -> 0 for black pixels
        pixelRow = np.empty(len(row), dtype=int)
        #print (len(pixelRow))
        for i in range(0, len(pixelRow)):
            if (row[i] == False):
                #print ("false")
                pixelRow[i] = 255
            elif (row[i] == True):
                #print ("true")
                pixelRow[i] = 0
            # print (pixelRow[i], row[i])
        return pixelRow

    # inverse function of pixelsToRow
    def pixelsToRow(self, pixelRow):
        row = np.empty(len(pixelRow), dtype=int)
        for i in range(0, len(row)):
            if (pixelRow[i] == 255):
                row[i] = False
            elif (pixelRow[i] == 0):
                row[i] = True
        return row

    def rowFromImage(self, rowNum):
        if (self.weaveFile != None and rowNum >= 0):
            row = self.weaveImg[rowNum, :]
            print ("got row with width", row.size)
            print (row)
            rowToSend = self.pixelsToRow(row)
            return rowToSend

    def weavePattern(self, patternArray):
        self.patternRow = self.lineNumber % len(patternArray) # fix this, pattern repeat should mod on number of rows since the pattern started, not the global number of rows
        rowToSend = self.patternToRow(patternArray)
        return rowToSend

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
    sys.exit(app.exec_())
