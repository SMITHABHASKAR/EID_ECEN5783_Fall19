# code modified from https://stackoverflow.com/questions/20873259/pyqt-how-to-dynamically-update-widget-property-on-outer-variable-value-change
import matplotlib.pyplot as plt
import random
import sys
import Adafruit_DHT
import numpy as np
import time
import datetime
import MySQLdb


from PyQt5 import QtCore, QtGui, QtWidgets #works for PyQt5
from integrated import Ui_Form #note the capitalization

conn = MySQLdb.connect(host= "localhost",user= "EID",passwd="EID",db="TEMP")
c=conn.cursor()

# main UI class
class Form(Ui_Form):
    # initialize function: set all tracked variables and start 15 second looped timer
    def __init__ (self, parent = None):
        super(Form, self).__init__ ()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # initialize values to track
        self.count = 0 # value of progress bar
        self.repeats = 0 # stop at 30
        self.temp_f = 0 # Fahrenheit reading
        self.temp_c = 0 # Celsius reading
        self.avgT = 0
        self.avgH = 0
        self.maxT = 0
        self.minT = 0
        self.mode = "F" # choose F or C
        self.ui.switchFC.setText(self.mode)
        self.graph = False # choose true (show graphs) or false (hide graphs)
        self.ui.showHideGraphs.setText("Show Graphs")
        #self.ui.tempGraph.canvas.ax.clear()
        #self.ui.tempGraph.canvas.ax.set_axis_off()
        #self.ui.humGraph.canvas.ax.clear()
        #self.ui.humGraph.canvas.ax.set_axis_off()
        self.hum = 0
        self.maxH = 0
        self.minH = 0
        #indexes for plotting
        self.temp_list = [0] * 10
        self.tempf_list = [0] * 10
        self.hum_list = [0] * 10
        self.idx_list = [0] * 10
        
        for i in range(10):
            self.idx_list[i] = i + 1
        
        self.ui.autoRefresh.setValue(self.count)
        self.timer = QtCore.QBasicTimer()
        self.timerEvent(64) # start timer

        self.scaleTemp()

        self.ui.humSet.setRange(15, 30)
        
        self.updateReadings()

    # rescale temperature sliders after switching F <--> C
    def scaleTemp(self):
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

    # take in current reading from sensor: temperature, humidity, datetime
    def sensor(self):
#        # uncomment if running with actual sensor
        sensor = Adafruit_DHT.DHT22
        pin = 4     # pin 7 on rpi 3 is GPIO 4
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        t_f=round((temperature*9)/5+32);
        #self.temp_f = (temperature*9)/5 + 32.0  
        self.temp_c = temperature
        self.hum = humidity
        self.temp_f = (temperature*9)/5 + 32.0 
        t_f=round((temperature*9)/5+32);
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

        c.execute("INSERT INTO SENSOR (DATEandTIME, TEMPERATUREinC,TEMPERATUREinF,HUMIDITY) VALUES (%s, %s, %s, %s)",(date, temperature, t_f, humidity))

        conn.commit()
#        c.close
#        conn.close()

        
        # uncomment if testing without sensor
        # humidity = 20
        # temperature = 30

        #error case
        if humidity is None or temperature is None:
            self.ui.status.setText('status: Sensor is not working!!!')
        else:
            self.ui.status.setText("status: Temperature - " + str(int(self.temp_f)) + "deg F / " + str(int(self.temp_c)) + "deg C || Humidity: " + str(int(self.hum)) + "% || Date/Time: " + date)
  

        # self.currTemp.setText('{0:0.1f} * C '.format(self.temp_c))
        # self.currTempinF.setText('{0:0.1f} * F '.format(self.temp_f))
        # self.currHum.setText('{0:0.1f} %  '.format(self.hum))
    
    # generate Temperature and Humidity graphs
    def plot_graph(self):
        self.ui.tempGraph.plot(self.idx_list, self.temp_list)
        plt = self.ui.tempGraph.canvas.ax
        self.ui.tempGraph.canvas.clear()

        plt.set_xlabel('Latest 10 values')
        
        if self.mode == "C":
            plt.set_ylabel('Temperature (Celsius)')
            plt.set_title('Temperature') #| Average = {0:0.1f} deg C
            plt.savefig('Temperature.png') #Saves the plots to be pulled up on the HTML
        elif self.mode == "F":
            plt.set_ylabel('Temperature (Fahrenheit)')
            plt.set_title('Temperature') # | Average = {0:0.1f} deg F.format(self.avgT).format(self.avgT)
        self.ui.tempGraph.canvas.draw()

        self.ui.humGraph.plot(self.idx_list, self.hum_list)        
        plt2 = self.ui.humGraph.canvas.ax
        self.ui.humGraph.canvas.clear()
        plt2.set_xlabel('Latest 10 values')
        plt2.set_ylabel('Humidity (%)')
        plt2.set_title('Humidity') #| Average = {0:0.1f} %.format(self.avgH)
        plt2.savefig('Humidity.png') #Saves the plots to be pulled up on the HTML
        self.ui.humGraph.canvas.draw()

    # pull current reading
    def button_pressed(self):
        self.sensor()
        #self.timerEvent(64) #this needs an argument to work but I'm not sure what is is yet so I just put in some random number

    # show or hide graphs
    def toggleGraphs(self):
        if self.graph == False:
            self.graph = True
            self.ui.showHideGraphs.setText("Hide Graphs")
            self.ui.tempGraph.show()
            self.ui.humGraph.show()
            self.plot_graph()
        elif self.graph == True:
            self.graph = False
            self.ui.showHideGraphs.setText("Show Graphs")
            self.ui.tempGraph.hide()
            self.ui.humGraph.hide()

    # switch between Fahrenheit (F) and Celsius (C)
    def toggleFC(self):
        if self.mode == "C":
            self.mode = "F"
            self.ui.switchFC.setText("F")
        elif self.mode == "F":
            self.mode = "C"
            self.ui.switchFC.setText("C")
        self.scaleTemp()

    # pull current reading and recalculate average
    def updateReadings(self):
        self.sensor()

        self.temp_list.pop(0)
        self.tempf_list.pop(0)
        self.hum_list.pop(0)    
        self.tempf_list.append(self.temp_f)
        
        self.temp_list.append(self.temp_c)
        
        self.hum_list.append(self.hum)
        
        # average value calculation
        self.avgT = sum(self.temp_list)/10
        self.avgH = sum(self.hum_list)/10
        self.avgTf = sum(self.tempf_list)/10
        
        self.updateTemp()
        self.updateHum()

    # update temperature readouts and check if out of bounds
    def updateTemp(self):
        # update temperature limits
        self.maxT = int(self.ui.tempSet.end())
        self.minT = int(self.ui.tempSet.start())
        
        print("acceptable range: " + str(self.minT) + "-" + str(self.maxT))
        
        # get latest reading and average
        if self.mode == "F":
            self.ui.currTemp.setProperty("intValue", self.temp_f)
        elif self.mode == "C":
            self.ui.currTemp.setProperty("intValue", self.temp_c)
        else:    
            return
        self.ui.avgTemp.setProperty("intValue", self.avgT)

        _currTemp = self.ui.currTemp.intValue()
        _avgTemp = self.ui.avgTemp.intValue()

        # check if current temp ok
        if _currTemp > self.maxT or _currTemp < self.minT:
            print("NO NO NO")
            self.ui.currTemp.setProperty("alert", True)
        else:
            print("just right")
            self.ui.currTemp.setProperty("alert", False)

        # check if avg temp ok
        if _avgTemp > self.maxT or _avgTemp < self.minT:
            self.ui.avgTemp.setProperty("alert", True)
        else:
            self.ui.avgTemp.setProperty("alert", False)
        
        self.ui.currTemp.setStyle(self.ui.currTemp.style())
        self.ui.avgTemp.setStyle(self.ui.avgTemp.style())

    # update humidity readouts and check if out of bounds
    def updateHum(self):
        #update humidity bounds
        self.minH = self.ui.humSet.start()
        self.maxH = self.ui.humSet.end()
        self.ui.currHum.setProperty("intValue", self.hum)
        self.ui.avgHum.setProperty("intValue", self.avgH)

        #check if current humidity ok
        if self.ui.currHum.intValue() < self.ui.humSet.start():
            self.ui.currHum.setProperty("alert", True)
        else:
            self.ui.currHum.setProperty("alert", False)
            
        #check if average humidity ok
        if self.ui.avgHum.intValue() < self.ui.humSet.start():
            self.ui.avgHum.setProperty("alert", True)
        else:
            self.ui.avgHum.setProperty("alert", False)
            
        self.ui.currHum.setStyle(self.ui.currTemp.style())
        self.ui.avgHum.setStyle(self.ui.avgTemp.style())

    # handle timerstart/increment/loop/stop
    def timerEvent(self, e):
        self.ui.autoRefresh.setValue(self.count)
        if self.count >=15:
            self.count = 0
            self.repeats += 1
            if self.repeats == 29:
                self.timer.stop()
            self.updateReadings()
            self.plot_graph()
        else:
            if self.timer.isActive():
                pass
            else:
                self.timer.start(1000,self) #10 milliseconds
        self.count+=1
        
    # temperature converting functions
    def FtoC(temp_f):
        return (temp_f - 32)*5/9
    def CtoF(temp_c):
        return temp_c*9/5 + 32