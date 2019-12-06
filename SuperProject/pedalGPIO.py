from gpiozero import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class pedalHandler(QObject):
    advancePedalEvent = pyqtSignal()
    refreshPedalEvent = pyqtSignal()
    reversePedalEvent = pyqtSignal()
    loomRelayEvent = pyqtSignal()
    
    def __init__(self, loom):
        # GPIO pins on Pi, all clustered on corner close to USB ports
        self.advancePedal = Button(16) # set to pull-up by default
        self.refreshPedal = Button(20)
        self.reversePedal = Button(21)
        self.loomRelay = DigitalOutputDevice(26)

        self.pedals = [self.advancePedal, self.refreshPedal, self.reversePedal]

        self.advancePedal.when_pressed = advancePressed
        self.advancePedal.when_released = advancePressed
        self.refreshPedal.when_pressed = refreshPressed
        self.refreshPedal.when_released = refreshPressed
        self.reversePedal.when_pressed = reversePressed
        self.reversePedal.when_released = reversePressed

    def advancePressed():
        print ("advance pedal pressed")
        advancePedalEvent.emit()
    def refreshPressed():
        print ("refresh pedal pressed")
        refreshPedalEvent.emit()
    def reversePressed():
        print ("reverse pedal pressed")
        reversePedalEvent.emit()

    def sendToRelay():
        print ("sending message to relay")
        self.loomRelay.blink(0.5, 0.5, 1) # turn on/off once to simulate pulse
        loomRelayEvent.emit()

if __name__ == "__main__":
    p = pedalHandler()
    pause()
