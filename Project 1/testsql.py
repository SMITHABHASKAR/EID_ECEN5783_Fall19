#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT
import MySQLdb
import datetime
from time import sleep

conn = MySQLdb.connect(host= "localhost",user= "EID",passwd="EID",db="TEMP")

c=conn.cursor()

sensor_args = { '11': Adafruit_DHT.DHT11,
                    '22': Adafruit_DHT.DHT22,
                    '2302': Adafruit_DHT.AM2302 }
    
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
                    sensor = sensor_args[sys.argv[1]]
                    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)
while True:
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    t_f=round((temperature*9)/5+32);

    if humidity is not None and temperature is not None:
        print('Temperature={0:0.1f}°C Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('SENSOR NOT WORKING!!!')
        sys.exit(1)

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

    c.execute("INSERT INTO SENSOR (DATEandTIME, TEMPERATUREinC,TEMPERATUREinF,HUMIDITY) VALUES (%s, %s, %s, %s)",(date, temperature, t_f, humidity))

    conn.commit()
    sleep(7.5)
    
c.close
conn.close()