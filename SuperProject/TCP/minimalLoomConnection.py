# Description: a minimal test loom GUI that provides buttons to connect to the loom
# You must be running the test TCP server to use the "fake loom" debugging ability. 
# (Otherwise it will have nothing to connect to and will error out.)

import math
import sys, os
from Loom import printOutput, Loom, LoomControl
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork

# diagnostic/debugging settings
realLoom = False # connect to a dummy TCP server
_MODULES = 6

# connection settings
port = 62000
ipAddress = "192.168.7.20"

class Ui_Form(QtWidgets.QMainWindow):
  def setupUi(self, Form):
    Form.setObjectName("Loom")
    Form.resize(500,300)

    self.loomControl = LoomControl()
    self.loomHandler = Loom(self.loomControl, _MODULES) # loom object?

    self.connectButton = QtWidgets.QPushButton(Form)
    self.connectButton.setGeometry(QtCore.QRect(10, 10, 100, 40))
    self.connectButton.setObjectName("connect")

    self.vacuum = QtWidgets.QPushButton(Form)
    self.vacuum.setGeometry(QtCore.QRect(120, 10, 100, 40))
    self.vacuum.setObjectName("vacuumToggle")
    #self.vacuum.setEnabled(False)

    self.terminal = QtWidgets.QTextEdit(Form)
    self.terminal.setGeometry(QtCore.QRect(10, 60, 480, 200))
    self.terminal.setObjectName("terminal")
    self.terminal.setReadOnly(True)

    self.retranslateUi(Form)

    #connections
    self.connectButton.clicked.connect(Form.connectLoom)
    self.vacuum.clicked.connect(Form.vacuum)
    self.loomControl.stateChanged.connect(printOutput)
    #self.loomControl.readyRead.connect(Form.logData)

    QtCore.QMetaObject.connectSlotsByName(Form)

  def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "Loom Connection"))
    self.connectButton.setText(_translate("Form", "Connect"))
    self.vacuum.setText(_translate("Form", "Vacuum Toggle"))

class Form(Ui_Form):
  def __init__ (self, parent = None):
    super(Form, self).__init__(parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)

    self.lineNumber = 0

  def connectLoom(self):
    # loom = Loom(false); 
    # second parameter is whether or not the loom is "real" -- 
    # use false for debugging (sending to the fake node loom; 
    # change to true to communicate with the actual loom
    if not realLoom:
      port = 1337
      ipAddress = '127.0.0.1'
    print ("making connection request")
    self.ui.loomControl.connectToHost(ipAddress, port)
    self.ui.loomControl.waitForConnected(2000)
    if (self.ui.loomControl.isConnected()):
      self.activateFunctions()
    else: print ("connection failed")

  def vacuum(self):
    print ("sending vacuum toggle")
    self.ui.loomHandler.toggleVacuum()

  def logData():
    newEntry = self.ui.loomHandler.readMessage()
    self.ui.terminal.append(newEntry)

  def activateFunctions():
    print ("connection successful!")
    self.ui.vacuum.setEnabled(True)

  def draw(self):
    if (self.loomHandler.askingForPick):
      print ("loom asking for pick")
      self.ui.loomHandler.sendPick(self.renderNextPick())

  def renderNextPick(self):
    self.lineNumber += 1
    print ("rendering next pick " + self.lineNumber)
    return self.tabby(1320, self.lineNumber)

  # loom takes picks as a list of 1 or 0. The first number in the list is the leftmost warp.
  # returns: int array
  def tabby(self, threads, rowNumber):
    pattern = []
    for i in range(0, threads):
      thread = 1;
      if (i%2 == rowNumber%2): 
        thread = 0

      pattern[i] = thread

    return pattern

# MAIN
if __name__ == "__main__":

    class AppWindow(QtWidgets.QDialog):
        def __init__(self): 
            super().__init__()
            self.ui = Ui_Form() 
            self.ui.setupUi(self)
            self.show()

    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    #t1 = threading.Thread(target=tornado_server)
    #t1.start()
    sys.exit(app.exec_())
    #t1.join()
