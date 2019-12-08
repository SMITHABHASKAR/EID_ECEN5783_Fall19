import sys, os, time
from gpiozero import *
from signal import pause
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class pedalHandler(QObject):
    advancePedalEvent = pyqtSignal()
    refreshPedalEvent = pyqtSignal()
    reversePedalEvent = pyqtSignal()
    loomRelayEvent = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # GPIO pins on Pi, all clustered on corner close to USB ports
        self.advancePedal = Button(16) # set to pull-up by default
        self.refreshPedal = Button(20)
        self.reversePedal = Button(21)
        self.loomRelay = DigitalOutputDevice(26)

        self.pedals = [self.advancePedal, self.refreshPedal, self.reversePedal]

        self.advancePedal.when_pressed = self.advancePressed
        self.advancePedal.when_released = self.advancePressed
        self.refreshPedal.when_pressed = self.refreshPressed
        self.refreshPedal.when_released = self.refreshPressed
        self.reversePedal.when_pressed = self.reversePressed
        self.reversePedal.when_released = self.reversePressed

    def advancePressed(self):
        print ("advance pedal pressed")
        self.advancePedalEvent.emit()
        self.sendToRelay()
    def refreshPressed(self):
        print ("refresh pedal pressed")
        self.refreshPedalEvent.emit()
        self.sendToRelay()
    def reversePressed(self):
        print ("reverse pedal pressed")
        self.reversePedalEvent.emit()
        self.sendToRelay()

    def sendToRelay(self):
        print ("sending message to relay")
        self.loomRelay.blink(0.3, 0.3, 1) # turn on/off once to simulate pedal step on/off
        self.loomRelayEvent.emit()

if __name__ == "__main__":
    class Ui_Form(QMainWindow):
        def setupUi(self, Form):
            Form.setObjectName("Pedal Testing with QT")
            Form.resize(800, 480)

            self.pedalHandler = pedalHandler()

            # advance pedal
            self.advance = QtWidgets.QPushButton(Form)
            self.advance.setGeometry(QtCore.QRect(440, 280, 60, 60))
            #self.advance.clicked.connect(Form.advance)

            # reverse pedal
            self.reverse = QtWidgets.QPushButton(Form)
            self.reverse.setGeometry(QtCore.QRect(300, 280, 60, 60))
            #self.reverse.clicked.connect(Form.reverse)

            # refresh pedal
            self.refresh = QtWidgets.QPushButton(Form)
            self.refresh.setGeometry(QtCore.QRect(370, 280, 60, 60))
            #self.refresh.clicked.connect(Form.refresh)

            self.pedals = [self.advance, self.reverse, self.refresh]

            self.pedalHandler.advancePedalEvent.connect(Form.advance)
            self.pedalHandler.refreshPedalEvent.connect(Form.refresh)
            self.pedalHandler.reversePedalEvent.connect(Form.reverse)
            self.pedalHandler.loomRelayEvent.connect(Form.pedalStep)
            
            self.retranslateUi(Form)
            
        def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Pedals in QT"))
            self.advance.setText(_translate("Form", "Next"))
            self.reverse.setText(_translate("Form", "Back"))
            self.refresh.setText(_translate("Form", "Again"))

    class Form(Ui_Form):
        def __init__(self, parent = None):
            super(Form, self).__init__(parent)
            self.ui = Ui_Form()
            self.ui.setupUi(self)

        def advance(self):
            print ("GUI: advance pedal pressed")
            self.ui.advance.setDown(True)
        def refresh(self):
            print ("GUI: refresh pedal pressed")
            self.ui.refresh.setDown(True)
        def reverse(self):
            print ("GUI: reverse pedal pressed")
            self.ui.reverse.setDown(True)

        def pedalStep(self):
            time.sleep(0.1)
            print ("GUI: sent signal to loom relay")
            for pedal in self.ui.pedals:
                if (pedal.isDown()):
                    pedal.setDown(False)
                    
    #p = pedalHandler()
    #pause()
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
