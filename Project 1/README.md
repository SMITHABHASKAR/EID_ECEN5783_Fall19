# EID PROJECT 1 - INTEGRATION OF DHT22 SENSOR WITH THE RPi3 AND QT INTERFACE

Developers: Smitha Bhaskar and Shanel Wu
With help from: Shubham Jaiswal
Instructor: Bruce Montgomery

## Installation Instructions

Execute the code by running:
python main.py (or python3 main.py)

Have the necessary libraries such as MySQL, Matplotlib, AdaFruit_DHT, PyQt5.
Citation:
1. https://www.mysql.com/downloads/
2. https://matplotlib.org
3. https://github.com/adafruit/Adafruit_Python_DHT 
4. https://build-system.fman.io/pyqt5-tutorial

## Project Work

We have designed a UI platform which is virtual replica of a thermostat. It is integrated with the Raspberry Pi 3 and the DHT22 sensor. The setup is as shown below. <Insert the photo of the setup>
  
It's an interactive UI, where in you can set the temperature and humidity range by interacting with the double-ended sliders for low and high bounds. When the sensor reading is out of the specified range, the interface will update you by turning the readings red and printing an alarm message. The sensor readings are collected and uploaded every 15 seconds to the database. The database looks like this: https://github.com/SMITHABHASKAR/EID_ECEN5783_Fall19/blob/master/Project%201/Project1-MySQL.PNG
The first column is the date and time, followed by: temperature in Celsius, temperature in Fahrenheit, and humidity. You can hide or show the graphs using the center button. The graphs are plotted based on the last 10 stored values from the tempertaure and humidity readings. However, if you are impatient and must simply know the temperature and humidity immediately, you can hit the "refresh" button to display the current status of the device in the status line. 

## Project Additions

As an additional feature, we have included a button for changing between degree C --> degree F, and vice-versa. The sliders, readouts, and the graphs are converted accordingly.

We included a custom QT Widget for the double-ended range slider, based off of another person's code. (see references for helpful links)

## References

1. [QRangeSlider Widget](https://stackoverflow.com/questions/47342158/porting-range-slider-widget-to-pyqt5) (which we modified into a vertical version)
2. [How to customize widget appearances](https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-using-dynamic-properties) and [how to dynamically update them](http://dgovil.com/blog/2017/02/24/qt_stylesheets/)
3. [How to define custom behaviors for widgets](https://stackoverflow.com/questions/20873259/pyqt-how-to-dynamically-update-widget-property-on-outer-variable-value-change)
4. [How to insert MatPlotLib figures in the main QT window](https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5)