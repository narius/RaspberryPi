# -*- coding: cp1252 -*-
#! /usr/bin/env python
import RPi.GPIO as GPIO
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import subprocess
import code
import sys
import time
import signal

def signal_handler(signal, frame):
    print "Exiting the script"
    lcd.clear()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#Initiate the LCD
lcd = Adafruit_CharLCDPlate()
lcd.clear()

output=subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
output=output.split("\n")
start=0
while True:
    if lcd.buttonPressed(lcd.DOWN):
        while lcd.buttonPressed(lcd.DOWN):
            pass
        lcd.clear()
        lcd.message("%s\n%s"%(output[start],output[start+1]))
        while not(lcd.buttonPressed(lcd.DOWN)  or lcd.buttonPressed(lcd.UP)):
            time.sleep(0.5)
            lcd.scrollDisplayLeft()
        if (start+1)<len(output):
            start+=1
    if lcd.buttonPressed(lcd.UP):
        while lcd.buttonPressed(lcd.UP):
            pass
        lcd.clear()
        lcd.message("%s\n%s"%(output[start],output[start+1]))
        while not(lcd.buttonPressed(lcd.DOWN) or lcd.buttonPressed(lcd.UP)):
            time.sleep(0.5)
            lcd.scrollDisplayLeft()
        if (start-1)>0:
            start-=1
            
        
