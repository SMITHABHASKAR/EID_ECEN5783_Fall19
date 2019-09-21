# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bestThermostat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from rangeslider_vert import QRangeSlider

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
#******************************************************************
import matplotlib
matplotlib.use("Qt5Agg")
#******************************************************************
from PyQt5 import QtCore 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

import sys 
import Adafruit_DHT
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime


        

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(922, 432)
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(380, 280, 101, 31))
        self.refresh.setObjectName("refresh")
        
        
         #indexes for plotting
        self.temp_list = [0] * 10
        self.hum_list = [0] * 10
        self.index_list = [0] * 10
        
        for i in range(10):
            self.idx_list[i] = i + 1

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
        self.tempSet.setRange(80) # fahrenheit
        self.tempSet.setObjectName("tempSet")

        # humidity slider
        self.humiditySet = QRangeSlider(Form)
        self.humiditySet.setGeometry(QtCore.QRect(760, 60, 30, 300))
        self.humiditySet.show()
        self.humiditySet.setRange(15, 35)
        self.humiditySet.setObjectName("humiditySet")

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
        self.autoRefresh.setInputMethodHints(QtCore.Qt.ImhNone)
        self.autoRefresh.setProperty("value", 24)
        self.autoRefresh.setObjectName("autoRefresh")

        self.retranslateUi(Form)
        self.refresh.clicked.connect(self.graphicsView.repaint)
        self.refresh.clicked.connect(self.label_2.update)
        self.refresh.clicked.connect(self.label.update)
        self.tempSet.valueChanged['int'].connect(self.widget.update)
        self.humiditySet.valueChanged['int'].connect(self.widget_2.update)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Best Thermostat"))
        self.refresh.setText(_translate("Form", "refresh"))
        self.label.setText(_translate("Form", "Temperature"))
        self.label_2.setText(_translate("Form", "Humidity"))
        self.label_3.setText(_translate("Form", "avg"))
        self.label_4.setText(_translate("Form", "avg"))
        
        
    def sensor(self):
        sensor = Adafruit_DHT.DHT22
        pin = 4     # pin 7 on rpi 3 is GPIO 4
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        
        # error case
#         if humidity is None or temperature is None:
#             self.label_7.setText('Sensor is not working!!!')
#         return
        self.temp_f = (temperature*9)/5 + 32.0  
        self.temp_c = temperature
        self.hum = humidity

        self.currTemp.setText('{0:0.1f} * C '.format(self.temp_c))
        self.currTempinF.setText('{0:0.1f} * F '.format(self.temp_f))
        self.currHum.setText('{0:0.1f} %  '.format(self.hum))
        
     # plot both the graphs after updating values
    def plot_graph(self):
        
        self.temp_list.pop(0)
        self.hum_list.pop(0)    
        self.temp_list.append(self.temp_c)
        self.hum_list.append(self.hum)
        
        # average value calculation
        tavg = sum(self.temp_list)/10
        havg = sum(self.hum_list)/10
        
        plt.clf()
        
        plt.subplot(311)
        plt.plot(self.index_list, self.temp_list)
        plt.xlabel('Latest 10 values')
        plt.ylabel('Temperature (Celcius)')
        plt.title('Live Temperature Graph | Average = {0:0.1f} deg Celcius'.format(tavg))
        plt.grid(True)
        
        plt.subplot(313)
        plt.plot(self.idx_list, self.hum_list)
        plt.xlabel('Latest 10 values')
        plt.ylabel('Humidity (%)')
        plt.title('Live Humidity Graph | Average = {0:0.1f} %'.format(havg))
        plt.grid(True)
        plt.draw()          
        plt.pause(0.001)
        plt.ion()
        plt.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Form()
    sys.exit(app.exec_())
        
        
        
        


