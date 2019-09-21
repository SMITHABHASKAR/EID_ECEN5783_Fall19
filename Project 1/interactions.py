# code modified from https://stackoverflow.com/questions/20873259/pyqt-how-to-dynamically-update-widget-property-on-outer-variable-value-change
import matplotlib.pyplot as plt
import random
import sys
import Adafruit_DHT
import numpy as np
import time
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets #works for PyQt5
from integrated import Ui_Form #note the capitalization

class Form(Ui_Form):
    def __init__ (self, parent = None):
        super(Form, self).__init__ ()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # initialize values to track
        self.count = 0 #Start value of progress bar
        self.temp_f = 0
        self.temp_c = 0
        self.avgT = 0
        self.avgH = 0
        self.maxT = 0
        self.minT = 0
        self.mode = "F" # choose F or C
        self.hum = 0
        self.maxH = 0
        self.minH = 0
        #indexes for plotting
        self.temp_list = [0] * 10
        self.hum_list = [0] * 10
        self.idx_list = [0] * 10
        
        for i in range(10):
            self.idx_list[i] = i + 1
        
        self.ui.autoRefresh.setValue(self.count)
        self.timer = QtCore.QBasicTimer()
        self.timerEvent(64) # start timer
        if self.mode == "F":
            self.ui.tempSet.setMin(0)
            self.ui.tempSet.setMax(120)
            self.ui.tempSet.setRange(65, 80)
        elif self.mode == "C":
            self.ui.tempSet.setMin(-10)
            self.ui.tempSet.setMax(50)
            self.ui.tempSet.setRange(20, 25)
        else:
            return

        self.ui.humSet.setRange(15, 35)
        
        self.updateReadings()

    def sensor(self):
        sensor = Adafruit_DHT.DHT22
        pin = 4     # pin 7 on rpi 3 is GPIO 4
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        
        #humidity = 20
        #temperature = 30

        # error case
#         if humidity is None or temperature is None:
#             self.label_7.setText('Sensor is not working!!!')
#         return
        self.temp_f = (temperature*9)/5 + 32.0  
        self.temp_c = temperature
        self.hum = humidity

        # self.currTemp.setText('{0:0.1f} * C '.format(self.temp_c))
        # self.currTempinF.setText('{0:0.1f} * F '.format(self.temp_f))
        # self.currHum.setText('{0:0.1f} %  '.format(self.hum))

    def plot_graph(self):
        
        self.temp_list.pop(0)
        self.hum_list.pop(0)    
        if self.mode == "F":
            self.temp_list.append(self.temp_f)
        elif self.mode == "C":
            self.temp_list.append(self.temp_c)
        else: return
        self.hum_list.append(self.hum)
        
        # average value calculation
        self.avgT = sum(self.temp_list)/10
        self.avgH = sum(self.hum_list)/10
        
        plt.clf()
        
        plt.subplot(311)
        plt.plot(self.idx_list, self.temp_list)
        plt.xlabel('Latest 10 values')
        plt.ylabel('Temperature (Celsius)')
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

    def button_pressed(self):
        self.updateReadings()
        self.timerEvent(64) #this needs an argument to work but I'm not sure what is is yet so I just put in some random number

    def updateReadings(self):
        self.sensor()
        self.updateTemp()
        self.updateHum()

    def updateTemp(self):
        # update temperature limits
        self.minT = self.ui.tempSet.end()
        self.maxT = self.ui.tempSet.start()
        
        # get latest reading and average
        if self.mode == "F":
            self.ui.currTemp.setProperty("intValue", self.temp_f)
        elif self.mode == "C":
            self.ui.currTemp.setProperty("intValue", self.temp_c)
        else:    
            return
        self.ui.avgTemp.setProperty("intValue", self.avgT)

        # check if current temp ok
        if self.ui.currTemp.intValue() > self.maxT or self.ui.currTemp.intValue() < self.minT:
            self.ui.currTemp.setProperty("alert", True)
        else:
            self.ui.currTemp.setProperty("alert", False)

        # check if avg temp ok
        if self.ui.avgTemp.intValue() > self.ui.tempSet.end() or self.ui.avgTemp.intValue() < self.ui.tempSet.start():
            self.ui.avgTemp.setProperty("alert", True)
        else:
            self.ui.avgTemp.setProperty("alert", False)

    def updateHum(self):
        self.ui.currHum.setProperty("intValue", self.hum)

        #check if current humidity ok
        if self.ui.currHum.intValue() < self.ui.humSet.start():
            self.ui.currHum.setProperty("alert", True)
        else:
            self.ui.currHum.setProperty("alert", False)

    def timerEvent(self, e):
        self.ui.autoRefresh.setValue(self.count)
        if self.count >=15:
            self.count = 0
            self.updateReadings()
        else:
            if self.timer.isActive():
                pass
            else:
                self.timer.start(1000,self) #10 milliseconds
        self.count+=1