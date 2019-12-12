# PyQT widgets for handling weaving patterns: displaying, editing, logging user input/progress, handling transactions with other devices/AWS cloud

import sys, os
import PIL as cv

from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from designFileEditing import * # Yarn, Pattern, Region, WeaveDesign

_BLOCKSIZE = 20

_TABBY = [[0, 1], [1, 0]]
_TWILL = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
_DOUBLE = [[0, 0, 0, 1], [0, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 1]]
_WAFFLE = [[0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0]]

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
#   - patternViewEdit = viewing the elements
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
        self.pattern = pattern # 2D int array or ndarray
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
        if (width > 0 and height > 0):
            emptyPattern = np.zeros((height, width), dtype=int)
            self.drawDraft(emptyPattern, True)

    def updateCell(self, row, col, data):
        if (self.pattern is not None):
            self.pattern[row][col] = data
            #print ("updated cell at", row, ",", col, "to", data)

    def setDraftWidth(self, newWidth):
        if (newWidth > 0):
            newPattern = np.zeros((self.patternHeight, newWidth), dtype=int)
            for row in range(0, len(newPattern)):
                for cell in range(0, len(newPattern[row])):
                    if (cell < len(self.pattern[row])):
                        newPattern[row][cell] = self.pattern[row][cell]
        #print ("resized pattern width:", newPattern)
        self.drawDraft(newPattern, True)

    def setDraftHeight(self, newHeight):
        if (newHeight > 0):
            newPattern = np.zeros((newHeight, self.patternWidth), dtype=int)
            for row in range(0, len(newPattern)):
                if (row < len(self.pattern)):
                    for cell in range(0, len(newPattern[row])):
                        newPattern[row][cell] = self.pattern[row][cell]
        self.drawDraft(newPattern, True)

    def resizeDraft(self, newWidth, newHeight):
        if (newWidth > 0 and newHeight > 0):
            newPattern = np.zeros((newHeight, newWidth), dtype=int)
            for row in range(0, len(newPattern)):
                if (row < len(self.pattern)):
                    for cell in range(0, len(newPattern[row])):
                        if (cell < len(self.pattern[row])):
                            newPattern[row][cell] = self.pattern[row][cell]
        print ("resized pattern:", newPattern)
    
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

# custom QDialog reference: https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
class saveDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        # INPUT: image file name
        self.saveImage = None
        self.text = QtWidgets.QLabel("Save your progress?")

        # BUTTONS: Save/Ok and Cancel
        self.buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.accepted.connect(self.getSaveImage)
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(self.text)
        layout.addWidget(self.buttons)

    def getSaveImage(self): 
        self.saveImage = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File As', "./weavingLog.bmp", "Image files (*.bmp)")
        return self.saveImage[0] # just return the file name, not the filter

    # return: whether or not the user saved, if the user rejected save dialog, still return something indicating that the UI had asked, so the user can quit without getting a message about "unsaved progress"
    @staticmethod
    def getSaveResult(parent=None):
        dialog = saveDialog(parent)
        result = dialog.exec_() # creates dialog as modal
        #print ("save dialog result:",result)
        fileName = dialog.saveImage
        return (fileName, result == QtWidgets.QDialog.Accepted)

class patternDialog(QtWidgets.QDialog):
    def __init__(self, name='', existing=None, parent=None): # can be initialized with an existing Pattern object to edit, instead of creating new
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.resize(300, 400)

        self.pattern = existing

        # INPUT: pattern name
        self.nameLabel = QLabel("Pattern name:")
        self.patternName = QLineEdit(self)

        # INPUT/DISPLAY: pattern graphics view
        self.draft = patternDraft()
        self.draftView = patternViewEdit(self)
        self.draftView.setScene(self.draft)

        # INPUTS: WIDTH x HEIGHT (QSpinBoxes)
        self.widthLabel = QLabel("Pattern width:")
        self.widthControl = QSpinBox(self)
        self.widthControl.setMinimum(0)
        self.widthControl.setMaximum(16) # not sure how wide of a pattern we can handle just yet
        #self.widthControl.resize(50, 20)

        self.heightLabel = QLabel("Pattern height:")        
        self.heightControl = QSpinBox(self)
        self.heightControl.setMinimum(0)
        self.heightControl.setMaximum(20)
        #self.heightControl.setGeometry()

        self.widthControl.valueChanged.connect(self.draft.setDraftWidth)
        self.heightControl.valueChanged.connect(self.draft.setDraftHeight)

        # set defaults if creating new pattern (existing = None)
        if (self.pattern is None):
            self.draft.drawBlankDraft(4, 4)
            self.pattern = self.draft.pattern
        else:
            self.draft.drawDraft(existing, True)
        
        self.widthControl.setValue(self.draft.patternWidth)
        self.heightControl.setValue(self.draft.patternHeight)
            

        # BUTTONS: Save/Ok and Cancel
        self.buttons = QtWidgets.QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.save = self.buttons.buttons()[0]
        self.save.setEnabled(False)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        
        self.patternName.textChanged.connect(self.validateSave)
        self.patternName.setText(name)
        
        for widget in [self.nameLabel, self.patternName, self.draftView, self.widthLabel, self.widthControl, self.heightLabel, self.heightControl, self.buttons]:
            layout.addWidget(widget)
            #widget.update()
        
    def validateSave(self):
        if (self.patternName.text() != ''):
            self.save.setEnabled(True)
        else:
            self.save.setEnabled(False)

    @staticmethod
    def createNewPattern(parent=None):
        dialog = patternDialog(None, parent)
        result = dialog.exec_()
        patternName = dialog.patternName.text()
        newPattern = dialog.draft.pattern
        return (patternName, newPattern, result == QtWidgets.QDialog.Accepted)

    @staticmethod
    def editPattern(existing, parent=None):
        dialog = patternDialog(existing, parent)
        result = dialog.exec_()
        patternName = dialog.patternName.text()
        editedPattern = dialog.draft.pattern
        return (patternName, editedPattern, result == QtWidgets.QDialog.Accepted)
            
if __name__ == '__main__':
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
    #patternName, newPattern, result = patternDialog.createNewPattern()
    #print ("pattern name:", patternName)
    #print ("new pattern data:", newPattern)
    #print ("result:", result)
    patternName, editedPattern, result = patternDialog.editPattern("Waffle weave", _WAFFLE)
    print ("pattern name:", patternName)
    print ("new pattern data:", editedPattern)
    print ("result:", result)
    
    sys.exit()
