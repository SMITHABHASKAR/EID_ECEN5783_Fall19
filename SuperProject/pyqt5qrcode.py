#Citation: https://www.codenov.com/1540126802d2d175d9162e3bc0fff233


import pyqrcode
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5 import QtCore,QtWidgets
from PIL import Image
import PIL
import qrcode.image.pil
from qrcode import *


 
class qrForm(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("LOOM GUI")
        QLabel().setText("welcome to Loom GUI Configuration")
        label=QLabel(self)
        
        #self.setGeometry(600,500,250,250)
        
               
 
        self.setMinimumSize(QtCore.QSize(600,800))
        self.setMaximumSize(QtCore.QSize(1500,900))
        self.resize(600,800)
        self.setGeometry(60,80,65,85)
        pixmap=QPixmap('logo.jpeg')
        label.setPixmap(pixmap)
#         self.resize(pixmap.width(),pixmap.height())
 
        self.centralwidget = QWidget(self)
        
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
 
        self.verticalLayout = QVBoxLayout()
 
        self.qrTextEdit = QLineEdit(self.centralwidget)
        self.verticalLayout.addWidget(self.qrTextEdit)
 
        self.genQrButton = QPushButton(self.centralwidget)
        self.genQrButton.setText("New User")
        self.verticalLayout.addWidget(self.genQrButton)
 
        self.decodeQrButton = QPushButton(self.centralwidget)
        self.decodeQrButton.setText("Scan QR Code")
        self.verticalLayout.addWidget(self.decodeQrButton)
 
        self.decodeText = QLabel(self.centralwidget)
        self.decodeText.setText("..")
        self.decodeText.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.decodeText)
 
        self.qrCodeImage = QLabel(self.centralwidget)
 
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.sizePolicy.setHorizontalStretch(1)
        self.sizePolicy.setVerticalStretch(1)
        self.sizePolicy.setHeightForWidth(self.qrCodeImage.sizePolicy().hasHeightForWidth())
 
        self.qrCodeImage.setSizePolicy(self.sizePolicy)
        self.qrCodeImage.setText("")
        self.qrCodeImage.setAlignment(QtCore.Qt.AlignCenter)
 
        self.verticalLayout.addWidget(self.qrCodeImage)
        self.horizontalLayout.addLayout(self.verticalLayout)
 
        self.setCentralWidget(self.centralwidget)
 
        self.genQrButton.clicked.connect(self.genButton)
        self.decodeQrButton.clicked.connect(self.decQrButton)
 
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open QRCode Image", "","Images (*.png);;All Files (*)", options=options)
        if fileName:
            return fileName
        else:
            return None
 
 
    def genButton(self):
        if(len(self.qrTextEdit.text()) < 1):
            return
        rQR = self.generateQR(self.qrTextEdit.text())
        self.qrCodeImage.setPixmap(QPixmap("test.png").scaled(429,429))
 
    def decQrButton(self):
        fswebcam image.jpg
        fName = self.openFileNameDialog()
        if (fName == None):
            return
        qr = decode(Image.open(fName), symbols=[ZBarSymbol.QRCODE])
        extractString = str(qr[0].data)
        self.decodeText.setText(extractString[2:-1])
 
    def generateQR(self,str):
        qr = QRCode(version = 4, box_size=5, border=0, error_correction=ERROR_CORRECT_L)
        qr.add_data(str)
        qr.make()
        qr.make(fit=True)
        im = qr.make_image(qrcode.image.pil.PilImage)
        width = 128
        height = 128
        im = im.resize((width, height), Image.ANTIALIAS)
        ext = ".png"
        im.save(str+ ext)
 
if __name__ == '__main__':
    sys._excepthook = sys.excepthook 
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback) 
        sys.exit(1) 
    sys.excepthook = exception_hook
    
    app = QApplication(sys.argv)
    pForm = qrForm()
    pForm.show()
    sys.exit(app.exec_())
