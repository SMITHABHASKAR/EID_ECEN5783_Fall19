from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QAction,QLineEdit,QMessageBox
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon,QPixmap
import sys


class App(QWidget):
       def __init__(self):
               super().__init__()
               self.title='Loom UI'
               self.left=10
               self.top=10
               self.width=640
               self.height=480
               self.initUI()
               QLabel().setText("welcome to Loom GUI Configuration")
       def initUI(self):
               self.setWindowTitle(self.title)
               label=QLabel(self)
               self.setGeometry(10,10,250,250)
               pixmap=QPixmap('logo.png')
               label.setPixmap(pixmap)
               self.resize(pixmap.width(),pixmap.height())
               self.setGeometry(self.left,self.top,self.width,self.height)
               self.button=QPushButton('New Project',self)
               self.button.clicked.connect(self.getText)
               self.button.move(100,200)
               
               #self.getText()
               button=QPushButton('Scan QR Code',self)               
               button.move(100,250)
               
               buttonexit=QPushButton('Close GUI',self)
               buttonexit.move(100,300)
               buttonexit.clicked.connect(self.buttonexit)
               self.show()
       @pyqtSlot()
       def getText(self):
           
           text, okPressed = QInputDialog.getText(self, "New Project Name","Your Project name:", QLineEdit.Normal, "")
           if okPressed and text != '':
               print(text)
               
       def buttonexit(self):
           
           QtCore.QCoreApplication.instance().quit()
           
if __name__=='__main__':
    app=QApplication(sys.argv)
    #sys.exit(app.exec_())
    ex=App()
