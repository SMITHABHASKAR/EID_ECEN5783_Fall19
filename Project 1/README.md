# EID PROJECT 1 - INTEGRATION OF DHT22 SENSOR WITH THE RPi3 AND QT INTERFACE

Developers: Smitha Bhaskar and Shanel Wu
With help from: Shubham Jaiswal
Instructor: Bruce Montgomery

## Installation Instructions

Execute the code by running:
python main.py

Have the necessary libraries such as MySQL, Matplotlib, AdaFruit_DHT, PyQt5.
Citation:
1. https://www.mysql.com/downloads/
2. https://matplotlib.org
3. https://github.com/adafruit/Adafruit_Python_DHT 
4. https://build-system.fman.io/pyqt5-tutorial

## Project Work

We have designed a UI platform which is virtual replica of a thermostat. It is integrated with the Raspberry Pi 3 and the DHT22 sensor. The setup is as shown below. <Insert the photo of the setup>
  
It's an interactive UI, where in you can set the temperature and humidity range, and when the sensor reading is out of range, it'll update you. It also displays the current status of the device in the status line. The sensor readings are updated every 15 seconds to the database. The database looks like this: https://github.com/SMITHABHASKAR/EID_ECEN5783_Fall19/blob/master/Project%201/Project1-MySQL.PNG
The first column is the date and time, followed by, temperature readings in degree C, degree Fahrenheit, humidity. 
The graph is plotted based on the last 10 values from the tempertaure and humidity readings. 

## Project Additions

As an additional facility, we have included a button for a change between degree C --> degree F , and vice-versa. The scrolling bar and the graph is update accordingly. 
