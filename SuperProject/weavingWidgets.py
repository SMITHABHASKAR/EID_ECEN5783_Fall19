# PyQT widgets for handling weaving patterns: displaying, editing, logging user input/progress, handling transactions with other devices/AWS cloud

from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from designFileEditing import * # Yarn, Pattern, Region, WeaveDesign

_BLOCKSIZE = 20

#   DISPLAY: Pattern selection, tracker, and editor
#   Appearance:
#   - If weaving from a pre-generated file, will be hidden (unless file has annotations with weave structures indicated)
#   Function:
#   - shows drawdown for the woven structure
#   - marker that shows place in the structure
#   - render pattern draft in QT for tracker
#   Organization:
#   - patternCell = the actual QRect elements
#   - patternDraft = organizing and listing the elements
#   - patternEditor = viewing the elements
#  references: https://stackoverflow.com/questions/39614777/how-to-draw-a-proper-grid-on-pyqt

class patternViewEdit(QtWidgets.QGraphicsView):
    patternChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.draft = patternDraft()
        self.setScene(self.draft)

        # connect user edits in the draft to anything outside of the widget
        
    def editingOn():
        self.draft.changed.connect(self.updatePattern)

    def editingOff():
        self.draft.changed.disconnect(self.updatePattern)

    def updatePattern():
        patternChanged.emit()

class patternCell(QtWidgets.QGraphicsRectItem):
    def __init__(self, col, row, y, size=_BLOCKSIZE, parent=None):
        super().__init__(col*size, y-size, size, size, parent)

        self.blackFill = QBrush(QColor(0, 0, 0))
        self.whiteFill = QBrush(QColor(255, 255, 255))

        self.col = col
        self.row = row
       
        self.data = False
        self.fill = self.whiteFill
        self.draft = None # when created and added to a draft, will be set to self.scene()

    def updateFill(self):
        if (self.data):
            self.fill = self.blackFill
        else:
            self.fill = self.whiteFill
        self.setBrush(self.fill)
 
    def mousePressEvent(self, event):
        # invert data and fill
        self.data = not self.data
        self.updateFill()
        self.draft.updateCell(self.row, self.col, self.data)

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

    def addCell(self, data, col, row, y, size, pen):
        cell = patternCell(col, row, y, size)
        cell.data = data
        cell.setPen(pen)
        cell.updateFill()
        #cell.draft = self # cell links back to draft to edit data
        self.addItem(cell)
        cell.draft = cell.scene()
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
                yc = (self.patternHeight - row) * self.blockSize
                data = pattern[row][cell] # 0 or 1
                if data is 1 or data is True:
                    fill = self.blackFill
                elif data is 0 or data is False:
                    fill = self.whiteFill
                self.squares[row][cell] = self.addCell(data, cell, row, yc, self.blockSize, self.linePen)        
                #if (not editing): # if this draft has been initiated in an editor
                    #self.squares[row][cell].setAcceptedMouseButtons(0)
                    #self.squares[row][cell].mousePressEvent.connect(self.updateCell)
        #print (self.squares)
        #print (self.items())

    def drawBlankDraft(self, width, height):
        if (width != 0 and height != 0):
            emptyPattern = np.zeros((height, width), dtype=int)
            self.drawDraft(emptyPattern, True)

    def updateCell(self, row, col, data):
        if (self.pattern != None):
            self.pattern[row][col] = data
            print ("updated cell at", row, ",", col, "to", data)
    
    def placeMarker(self, row):
        print ("placing marker on row", row)
        xm = -1*_BLOCKSIZE
        ym = (self.patternHeight-row-1)*self.blockSize
        if (self.marker is None):
            # create the marker
            self.marker = self.addRect(xm, ym, self.width + 2*self.blockSize, self.blockSize, self.noLine, self.highlight)
            print ("created marker at", ym)
        else:
            self.marker.setY(-row*self.blockSize)
            print ("ym =",ym)
            print ("marker y =", -row*self.blockSize)
            print ("scene y = ",self.marker.mapFromScene(xm, ym).y())
        #print (self.marker)

#   DISPLAY: Design file/log viewer and progress tracker
#   Appearance:
#   - If weaving from a file, show the full file and a marker where the weaver currently is in the design AND expand to fill width of UI
#   - If generating a file as-you-go, show the logged file so far and a marker at the last row AND make room for the pattern tracker
#   Organization:
#   - projectProgress = scene holding the loaded file image and progress marker

class projectProgress(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.squares = [] # elements in the scene
        self.design = None # A QPixmap
        self.blockSize = 2 # TODO: change to the scale of the displayed design
        self.designHeight = 0 # number of rows in design
        self.designWidth = 0 # should be 1320

        self.marker = None # marker rectangle during weaving

        self.noLine = QPen(QColor(0,0,0,0)) # no line
        self.highlight = QBrush(QColor(255, 0, 0, 200)) # translucent yellow

    def setDesign(self, designFile):
        self.design = designFile
        self.designHeight = designFile.height()
        self.designWidth = designFile.width()

    def placeMarker(self, row):
        xm = -1 * self.blockSize
        ym = (self.designHeight - row - 1) * self.blockSize # rows are numbered from bottom to top, marker should start on bottom of image
        if (self.marker is None):
            # create the marker
            self.marker = self.addRect(xm, ym, self.width() + 2*self.blockSize, self.blockSize, self.noLine, self.highlight)
        else:
            self.marker.setY(-row*self.blockSize)
