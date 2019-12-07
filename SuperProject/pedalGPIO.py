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
    p = pedalHandler()
    pause()
