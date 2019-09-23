# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bestThermostat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from rangeslider_vert import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('QT5Agg')

# custom classes modified from https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5
# to plot the 
class Graph(Canvas):
    def __init__(self, parent=None):
        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        Canvas.__init__(self, self.figure)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

class MPLWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = Graph()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        #self.plot()
        
    def plot(self, Xdata, Ydata):
        #data = [random.random() for i in range(10)]
        
        self.canvas.ax.clear()
        self.canvas.ax.plot(Xdata, Ydata, '*-')
        self.canvas.draw()

class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 400)
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(310, 280, 101, 31))
        self.refresh.setObjectName("refresh")

        self.status = QtWidgets.QLabel(Form)
        self.status.setGeometry(QtCore.QRect(25, 25, 650, 31))
        self.status.setObjectName("statusMessage")
                                
        # temperature graph
        self.tempGraph = MPLWidget(Form)
        self.tempGraph.show()
        self.tempGraph.setGeometry(QtCore.QRect(100, 30, 256, 192))
        self.tempGraph.setObjectName("tempGraph")

        # humidity graph
        self.humGraph = MPLWidget(Form)
        self.humGraph.show()
        self.humGraph.setGeometry(QtCore.QRect(380, 30, 256, 192))
        self.humGraph.setObjectName("humGraph")

        # temperature slider
        self.tempSet = QRangeSlider(Form)
        self.tempSet.setGeometry(QtCore.QRect(20, 60, 30, 300))
        self.tempSet.show()
        self.tempSet.setObjectName("tempSet")

        # humidity slider
        self.humSet = QRangeSlider(Form)
        self.humSet.setGeometry(QtCore.QRect(690, 60, 30, 300))
        self.humSet.show()
        self.humSet.setObjectName("humSet")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(5, 371, 101, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(670, 360, 71, 21))
        self.label_2.setObjectName("label_2")
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(100, 240, 120, 121))
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet("QLCDNumber[alert=true]{background: rgb(255, 0, 0)}")
        self.widget.setObjectName("widget")

        self.avgTemp = QtWidgets.QLCDNumber(self.widget)
        self.avgTemp.setGeometry(QtCore.QRect(50, 90, 64, 23))
        self.avgTemp.setDigitCount(3)
        self.avgTemp.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        #self.avgTemp.setProperty("intValue", 73)
        self.avgTemp.setProperty("min", 65)
        self.avgTemp.setProperty("max", 85)
        self.avgTemp.setProperty("alert", False)
        self.avgTemp.setObjectName("avgTemp")
        self.currTemp = QtWidgets.QLCDNumber(self.widget)
        self.currTemp.setGeometry(QtCore.QRect(20, 30, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.currTemp.setFont(font)
        self.currTemp.setAutoFillBackground(False)
        self.currTemp.setDigitCount(3)
        self.currTemp.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        #self.currTemp.setProperty("intValue", 80)
        self.currTemp.setProperty("min", 65)
        self.currTemp.setProperty("max", 85)
        self.currTemp.setProperty("alert", False)
        self.currTemp.setObjectName("currTemp")
        self.currTemp.show()
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 31, 22))
        self.label_3.setObjectName("label_3")

        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(510, 240, 120, 121))
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("QLCDNumber[alert=true]{background: rgb(255, 0, 0)}")
        self.avgHum = QtWidgets.QLCDNumber(self.widget_2)
        self.avgHum.setGeometry(QtCore.QRect(50, 90, 64, 23))
        self.avgHum.setDigitCount(3)
        self.avgHum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        #self.avgHum.setProperty("intValue", 27)
        self.avgHum.setObjectName("avgHum")
        self.currHum = QtWidgets.QLCDNumber(self.widget_2)
        self.currHum.setGeometry(QtCore.QRect(20, 30, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.currHum.setFont(font)
        self.currHum.setDigitCount(3)
        self.currHum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        #self.currHum.setProperty("intValue", 30)
        self.currHum.setObjectName("currHum")
        self.currHum.show()
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 31, 22))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(632, 272, 20, 31))
        
        self.autoRefresh = QtWidgets.QProgressBar(Form)
        self.autoRefresh.setGeometry(QtCore.QRect(310, 320, 101, 16))
        self.autoRefresh.setMaximum(15)
        self.autoRefresh.setProperty("value", 0)
        self.autoRefresh.setObjectName("autoRefresh")

        self.showHideGraphs = QtWidgets.QPushButton(Form)
        self.showHideGraphs.setGeometry(QtCore.QRect(310, 230, 101, 31))
        self.showHideGraphs.setObjectName("showHideGraphs")

        self.switchFC = QtWidgets.QPushButton(Form)
        self.switchFC.setGeometry(QtCore.QRect(222, 272, 51, 31))
        self.switchFC.setObjectName("switchFC")

        self.retranslateUi(Form)

        # connections here
        self.refresh.clicked.connect(Form.button_pressed)
        self.showHideGraphs.clicked.connect(Form.toggleGraphs)
        self.switchFC.clicked.connect(Form.toggleFC)
        self.tempSet.startValueChanged['int'].connect(Form.updateTemp)
        self.tempSet.endValueChanged['int'].connect(Form.updateTemp)
        self.humSet.startValueChanged['int'].connect(Form.updateHum)
        self.humSet.endValueChanged['int'].connect(Form.updateHum)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Best Thermostat"))
        self.refresh.setText(_translate("Form", "refresh"))
        self.status.setText(_translate("Form", "status: "))
        self.label.setText(_translate("Form", "Temperature"))
        self.label_2.setText(_translate("Form", "Humidity"))
        self.label_3.setText(_translate("Form", "avg"))
        self.label_4.setText(_translate("Form", "avg"))
        self.label_5.setText(_translate("Form", "%"))


