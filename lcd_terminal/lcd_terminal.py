# -*- coding: cp1252 -*-
#! /usr/bin/env python
import RPi.GPIO as GPIO
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import subprocess
import code
import sys
import time

#Initiate the LCD
lcd = Adafruit_CharLCDPlate()
lcd.clear()

output=subprocess.Popen(["ls"], stdout=subprocess.PIPE).communicate()[0]
output=output.split("\n")
start=0
try:
    while True:
        if lcd.buttonPressed(lcd.DOWN):
            while lcd.buttonPressed(lcd.DOWN):
                pass
            lcd.clear()
            lcd.message("%s\n%s"%(output[start],output[start+1]))
            while not(lcd.buttonPressed(lcd.DOWN)):
                time.sleep(0.5)
                lcd.scrollDisplayLeft()
            start+=1
            
            
except KeyboardInterrupt: #The program will run until ctrl-c is pressed
    lcd.clear()
        
