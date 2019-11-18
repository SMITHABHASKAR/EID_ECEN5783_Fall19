# Description: a minimal test loom GUI that provides buttons to connect to the loom
# You must be running the test TCP server to use the "fake loom" debugging ability. 
# (Otherwise it will have nothing to connect to and will error out.)

import math
import sys, os
import asyncio
from Loom import printOutput, Loom
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import pyqtSlot

# diagnostic/debugging settings
realLoom = True # connect to a dummy TCP server
_MODULES = 6

# connection settings
_PORT = 62000
_IPADDRESS = '192.168.7.20'

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
    self.terminal.setGeometry(QtCore.QRect(10, 60, 480, 200))
    self.terminal.setObjectName("terminal")
    self.terminal.setReadOnly(True)

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
    self.advance.setGeometry(QtCore.QRect(220, 280, 60, 60))
    self.advance.setEnabled(False)
    self.advance.setVisible(False) # hidden until started = true

    self.activeFunctions = [self.vacuum, self.tabby, self.stop, self.advance]

    self.retranslateUi(Form)

    #button connections
    self.connectButton.clicked.connect(Form.connectLoom)
    self.vacuum.clicked.connect(Form.vacuum)
    self.tabby.clicked.connect(Form.updateLoomState)
    self.stop.clicked.connect(Form.stopLoom)
    self.advance.clicked.connect(Form.draw)

    #loom events
    self.loomHandler.messageFromLoom.connect(Form.logData)
    self.loomHandler.loomConnected.connect(Form.activateUI)
    self.loomHandler.loomDisconnected.connect(Form.deactivateUI)
    self.loomHandler.pickRequest.connect(Form.draw)

    QtCore.QMetaObject.connectSlotsByName(Form)

  def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "Loom Connection"))
    self.connectButton.setText(_translate("Form", "Connect"))
    self.vacuum.setText(_translate("Form", "Vacuum Toggle"))
    self.tabby.setText(_translate("Form", "Start Tabby"))
    self.stop.setText(_translate("Form", "Stop"))
    self.advance.setText(_translate("Form", "Next"))

class Form(Ui_Form):
  def __init__ (self, parent = None):
    super(Form, self).__init__(parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)

    self.lineNumber = 0
    self.loomConnected = False
    self.vacuumOn = False
    self.loomState = "stopped" # stopped, started, paused

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
      self.ui.advance.setVisible(True) # started weaving, pedal is available
      self.ui.advance.setEnabled(True)
      self.ui.stop.setVisible(False)
      self.loomState = "started"
      self.ui.tabby.setText("Pause")
      self.vacuum()
      self.draw() # weaver can step on the pedal, "next" button not necessary
    elif (self.loomState == "started"): # transition from started to paused
      self.loomState = "paused"
      self.vacuum()
      # need to resend current pick here, did not advance
      self.ui.tabby.setText("Resume")
      self.ui.advance.setEnabled(False) # disable pedal
      self.ui.stop.setVisible(True)
  
  def stopLoom(self):
    self.loomState = "stopped"
    if (self.vacuumOn):
      self.vacuum()
    self.ui.advance.setVisible(False)
    self.ui.stop.setVisible(False)
    self.ui.tabby.setText("Start Tabby")

  def draw(self):
    #if (self.loomHandler.askingForPick):
      #print ("loom asking for pick")
    self.ui.loomHandler.sendPick(self.renderNextPick())

  def renderNextPick(self):
    self.lineNumber += 1
    self.ui.terminal.append("rendering next pick " + str(self.lineNumber))
    return self.tabby(1320, self.lineNumber)

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
    #asyncio.run(w.ui.loomHandler.loomcontrol.keepConnection())
    #t1 = threading.Thread(target=tornado_server)
    #t1.start()
    #t1.join()

