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

sys.path.insert(1, './TCP') # Loom.py is in the TCP folder
sys.path.insert(1, './testFiles') # access test images

from Loom import Loom
from minimalLoomConnection import * # use the functions already built in this file

# simple woven patterns for testing, store as a list of lists or AxB matrix
# for example, plainweave represents:   0   1 
#                                       1   0 
_TABBY = [[0, 1], [1, 0]]
_TWILL = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
_DOUBLE = [[0, 0, 0, 1], [0, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 1]]
_WAFFLE = [[0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0]]

_patternOptions = [["Tabby",_TABBY], ["Twill",_TWILL], ["Doubleweave", _DOUBLE], ["Waffle",_WAFFLE]]

# yarns listed as [ SHORTCODE, HEX_COLOR ]
yarn = [] # if yarn list is blank, fill with default yarn ['A', '0xFFFFFF'] (yarn A, white color)
twoYarns = [['A', '0xFFFFFF'], ['B', '0xFF0000']]

_ROWWIDTH = 1320
_BLOCKSIZE = 20

# diagnostic/debugging settings
realLoom = True # connect to a dummy TCP server if False
_MODULES = 6

# connection settings
_PORT = 62000
_IPADDRESS = '192.168.7.20'

class patternEditor(QtWidgets.QGraphicsView):
    def __init__(self, pattern=None, parent=None):
        super().__init__(parent)

        self.draft = patternDraft()
        self.setScene(self.draft)

        if (pattern is not None):
            self.draft.drawDraft(pattern, True)

    #def draw

class patternCell(QtWidgets.QGraphicsRectItem):
    def __init__(self, col, row, size=_BLOCKSIZE, parent=None):
        super().__init__(col*size, row*size, size, size, parent)

        self.blackFill = QBrush(QColor(0, 0, 0))
        self.whiteFill = QBrush(QColor(255, 255, 255))

        self.col = col
        self.row = row
       
        self.data = False
        self.fill = self.whiteFill
        self.draft = None
 
    def mousePressEvent(self, event):
        self.data = not self.data
        if (self.fill == self.whiteFill):
            self.fill = self.blackFill
        else:
            self.fill = self.whiteFill
        self.setBrush(self.fill)
        if (self.draft != None):
            self.draft.pattern[self.row][self.col] = self.data

#   DISPLAY: Pattern repeat tracker
#   Function/Appearance:
#   - shows drawdown for the woven structure
#   - marker that shows place in the structure
#   - render pattern draft in QT for tracker
# references: https://stackoverflow.com/questions/39614777/how-to-draw-a-proper-grid-on-pyqt
class patternDraft(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.squares = [] # elements in the scene
        self.pattern = None
        self.blockSize = _BLOCKSIZE
        self.patternHeight = 0
        self.patternWidth = 0

        self.marker = None # marker rectangle during weaving

        # styles for rendering
        self.linePen = QPen(QColor(128, 128, 128), 3) # gray line w/ weight 4
        self.noLine = QPen(QColor(0,0,0,0)) # no line
        self.blackFill = QBrush(QColor(0, 0, 0))
        self.whiteFill = QBrush(QColor(255, 255, 255))
        self.highlight = QBrush(QColor(255, 255, 0, 100)) # translucent yellow

    def addCell(self, data, x, y, size, pen, fill):
        cell = patternCell(x, y, size)
        cell.data = data
        cell.setPen(pen)
        cell.setBrush(fill)
        cell.draft = self # cell links back to draft to edit data
        self.addItem(cell)
        return cell
        
    def drawDraft(self, pattern, editing=True):
        self.clear()
        self.marker = None
        self.pattern = pattern # 2D int array
        #print (self.pattern)

        self.patternHeight = len(pattern)
        self.patternWidth = len(pattern[0])
    
        self.squares = [[None]*self.patternWidth]*self.patternHeight # copy pattern list's shape
        #print (self.squares)
        self.width = self.patternWidth * self.blockSize
        self.height = self.patternHeight * self.blockSize
        self.setSceneRect(0, 0, self.width, self.height)
        self.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        
        for row in range(0, len(self.pattern)):
            for cell in range(0, len(pattern[row])):
                xc = cell * self.blockSize
                yc = row * self.blockSize
                data = pattern[row][cell] # 0 or 1
                if data is 1 or data is True:
                    fill = self.blackFill
                elif data is 0 or data is False:
                    fill = self.whiteFill
                self.squares[row][cell] = self.addCell(data, cell, row, self.blockSize, self.linePen, fill)        
                #if (not editing): # if this draft has been initiated in an editor
                    #self.squares[row][cell].setAcceptedMouseButtons(0)
                    #self.squares[row][cell].mousePressEvent.connect(self.updateCell)
        #print (self.squares)
        #print (self.items())

    def drawBlankDraft(self, width, height):
        if (width != 0 and height != 0):
            emptyPattern = np.zeros((height, width), dtype=int)
            self.drawDraft(emptyPattern, True)
            
    #def mousePressEvent(self, event):
    #    self.updateCell(event)
    #    print (self.mouseGrabberItem())

    def updateCell(self, event):
        print ("cell clicked at", event.scenePos().x(), ",", event.scenePos().y())
    
    def placeMarker(self, row):
        xm = -1*_BLOCKSIZE
        ym = row * _BLOCKSIZE
        if (self.marker is None):
            # create the marker
            self.marker = self.addRect(xm, ym, self.width + 2*_BLOCKSIZE, _BLOCKSIZE, self.noLine, self.highlight)
        else:
            self.marker.setY(ym)
        #print (self.marker)
    
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
        Form.resize(800,350)

        self.loomHandler = Loom(_MODULES)

        self.connectButton = QtWidgets.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(10, 10, 100, 40))
        self.connectButton.setObjectName("connect")
        self.connectButton.clicked.connect(Form.connectLoom)

        # display widgets: terminal, draft view, overall project view

        self.terminal = QtWidgets.QTextEdit(Form)
        self.terminal.setGeometry(QtCore.QRect(270, 60, 210, 210))
        self.terminal.setObjectName("terminal")
        self.terminal.setReadOnly(True)
        self.terminal.setVisible(False)

        self.draft = patternDraft()
        self.draftView = QtWidgets.QGraphicsView(self.draft, Form)
        self.draftView.setGeometry(QtCore.QRect(10, 70, 200, 200))
        self.draftView.setScene(self.draft)

        self.projectView = QtWidgets.QGraphicsView(Form)
        self.projectView.setGeometry(QtCore.QRect(220, 60, 550, 210))
        self.projViewLabel = QtWidgets.QLabel(self.projectView)
        self.projViewLabel.setGeometry(QtCore.QRect(0, 0, 550, 210))

        # editing functions

        self.selectPattern = QtWidgets.QComboBox(Form)
        self.selectPattern.setGeometry(QtCore.QRect(10, 60, 200, 30))
        self.selectPattern.addItem("Select pattern")
        #for pattern in _patternOptions:
        #    self.selectPattern.addItem(pattern[0])
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
        self.advance.setGeometry(QtCore.QRect(290, 280, 60, 60))
        self.advance.clicked.connect(Form.advance)

        # reverse pedal
        self.reverse = QtWidgets.QPushButton(Form)
        self.reverse.setGeometry(QtCore.QRect(150, 280, 60, 60))
        self.reverse.clicked.connect(Form.reverse)

        # refresh pedal
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(220, 280, 60, 60))
        self.refresh.clicked.connect(Form.sendToLoom)

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
        self.loomHandler.pickRequest.connect(Form.advance)
        self.loomHandler.vacuumChanged.connect(Form.sendToLoom)

        QtCore.QMetaObject.connectSlotsByName(Form)
        self.retranslateUi(Form)

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
        self.weaveFile = None

        self.loomConnected = False
        self.vacuumOn = False
        self.loomState = "stopped" # stopped, started, paused

        self.loadPatternFile()

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

    def loadWeaveFile(self):
        # open QFileDialog
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Image files (*.bmp *.tif)")
        print (file) # tuple ('file path', 'ext')
        if (file[0] is not ''):
            print ("user loaded file")
            self.weaveFile = QPixmap(file[0])
            self.ui.projViewLabel.setPixmap(self.weaveFile)
        else: print ("user cancelled")

    def updatePatternSelected(self, pattern):
        #print (pattern)
        #if (pattern is 1):
        #    self.patternSelected = _TABBY
        #elif (pattern is 2):
        #    self.patternSelected = _TWILL
        #elif (pattern is 3):
        #    self.patternSelected = _WAFFLE
        self.patternSelected = self.patternList[pattern-1]['pattern']#_patternOptions[pattern-1][1]
        
        self.ui.draftView.setScene(self.ui.draft)
        self.ui.draft.drawDraft(self.patternSelected, True)

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
        img = imgarr.array2qimage(self.weavingLog) # a QtGui.QImage
        pixmap = QtGui.QPixmap(img)
        pixmap.setDevicePixelRatio(0.5) # set pixmap raio = half of real image -> pixmap pixels are magnified 2x
        self.ui.projViewLabel.setPixmap(pixmap)

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
            if (self.patternSelected is not None):
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
        if (self.vacuumOn):
            self.vacuum()
        for pedal in self.ui.pedals:
            pedal.setVisible(False)
        self.ui.stop.setVisible(False)
        self.ui.start.setText("Start")
        # for now, also saves the weaving log image
        if (self.logging):
            cv.imwrite('testWeavingLog.bmp', self.weavingLog)

    def advance(self):
        #if (self.loomHandler.askingForPick):
          #print ("loom asking for pick")
        self.lineNumber += 1
        self.rowBuffer = self.renderNextPick()
        self.sendToLoom()
        self.ui.draft.placeMarker(self.patternRow)        

    def reverse(self):
        self.lineNumber -= 1
        self.rowBuffer = self.renderNextPick()
        self.sendToLoom()
        self.ui.draft.placeMarker(self.patternRow)        

    def sendToLoom(self, copy=True):
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

    def renderNextPick(self):
        self.ui.terminal.append("rendering pick " + str(self.lineNumber))
        #return self.tabby(1320, self.lineNumber)
        #return self.weavePattern(_TWILL)
        return self.weavePattern(self.patternSelected)

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

    # weaving other patterns
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

    def rowFromImage(self):
        # TODO: fix this
        rowToSend = self.rowBuffer
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
    app.exec_()
