import sys, os
from PyQt5.QtWidgets import QDialog, QApplication # case sensitive!
from integrated import *
from interactions import *

class AppWindow(QDialog):
    def __init__(self): 
        super().__init__()
        self.ui = Ui_Form() # Class name from bestThermostat.py
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = Form()
w.show()
sys.exit(app.exec_())