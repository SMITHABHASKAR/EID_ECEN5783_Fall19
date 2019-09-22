# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bestThermostat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from rangeslider_vert import QRangeSlider

class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(922, 432)
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(380, 280, 101, 31))
        self.refresh.setObjectName("refresh")

        # temperature graph
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(170, 30, 256, 192))
        self.graphicsView.setObjectName("graphicsView")

        # humidity graph
        self.graphicsView_2 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(450, 30, 256, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")

        # temperature slider
        self.tempSet = QRangeSlider(Form)
        self.tempSet.setGeometry(QtCore.QRect(90, 60, 30, 300))
        self.tempSet.show()
        self.tempSet.setRange(65, 80) # fahrenheit
        self.tempSet.setObjectName("tempSet")

        # humidity slider
        self.humSet = QRangeSlider(Form)
        self.humSet.setGeometry(QtCore.QRect(760, 60, 30, 300))
        self.humSet.show()
        self.humSet.setRange(15, 35)
        self.humSet.setObjectName("humiditySet")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 371, 101, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(740, 360, 71, 21))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(170, 240, 120, 121))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QLCDNumber[alert=true]{background: rgb(255, 0, 0)}")
        self.widget.setObjectName("widget")

        self.avgTemp = QtWidgets.QLCDNumber(self.widget)
        self.avgTemp.setGeometry(QtCore.QRect(50, 90, 64, 23))
        self.avgTemp.setDigitCount(3)
        self.avgTemp.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.avgTemp.setProperty("intValue", 73)
        self.avgTemp.setObjectName("avgTemp")
        self.currTemp = QtWidgets.QLCDNumber(self.widget)
        self.currTemp.setGeometry(QtCore.QRect(20, 30, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.currTemp.setFont(font)
        self.currTemp.setAutoFillBackground(False)
        self.currTemp.setDigitCount(3)
        self.currTemp.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currTemp.setProperty("intValue", 80)
        self.currTemp.setProperty("min", 65)
        self.currTemp.setProperty("max", 85)
        self.currTemp.setProperty("alert", False)
        self.currTemp.setObjectName("currTemp")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 31, 22))
        self.label_3.setObjectName("label_3")

        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(580, 240, 120, 121))
        self.widget_2.setObjectName("widget_2")
        self.avgHum = QtWidgets.QLCDNumber(self.widget_2)
        self.avgHum.setGeometry(QtCore.QRect(50, 90, 64, 23))
        self.avgHum.setStyleSheet("QLCDNumber[alert=true]{background: rgb(255, 0, 0)}")
        self.avgHum.setDigitCount(3)
        self.avgHum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.avgHum.setProperty("intValue", 27)
        self.avgHum.setObjectName("avgHum")
        self.currHum = QtWidgets.QLCDNumber(self.widget_2)
        self.currHum.setGeometry(QtCore.QRect(23, 30, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.currHum.setFont(font)
        self.currHum.setDigitCount(3)
        self.currHum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currHum.setProperty("intValue", 30)
        self.currHum.setObjectName("currHum")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 31, 22))
        self.label_4.setObjectName("label_4")
        self.autoRefresh = QtWidgets.QProgressBar(Form)
        self.autoRefresh.setGeometry(QtCore.QRect(380, 320, 101, 16))
        self.autoRefresh.setMaximum(15)
        self.autoRefresh.setProperty("value", 0)
        self.autoRefresh.setObjectName("autoRefresh")

        self.retranslateUi(Form)
        self.refresh.clicked.connect(Form.button_pressed)
        self.tempSet.startValueChanged['int'].connect(Form.updateTemp)
        self.tempSet.endValueChanged['int'].connect(Form.updateTemp)
        self.humSet.startValueChanged['int'].connect(Form.updateHum)
        self.humSet.endValueChanged['int'].connect(Form.updateHum)
        # self.refresh.clicked.connect(self.graphicsView.repaint)
        # self.refresh.clicked.connect(self.label_2.update)
        # self.refresh.clicked.connect(self.label.update)
        # self.tempSet.startValueChanged['int'].connect(Form.update)
        #self.humiditySet.valueChanged['int'].connect(self.widget_2.update)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Best Thermostat"))
        self.refresh.setText(_translate("Form", "refresh"))
        self.label.setText(_translate("Form", "Temperature"))
        self.label_2.setText(_translate("Form", "Humidity"))
        self.label_3.setText(_translate("Form", "avg"))
        self.label_4.setText(_translate("Form", "avg"))


