# -*- coding: cp1252 -*-
#utveckling för att använda fler LED
import RPi.GPIO as GPIO
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from class_led import Led

GPIO.setmode(GPIO.BCM)

leds=[Led(17), Led(27),Led(23)]
selected_led=0
number_of_leds=len(leds)
#Initierar lcd
lcd = Adafruit_CharLCDPlate()
lcd.clear()

lcd.message(leds[0].getStatus())
try:
    while True:
    #lcd.clear()
    #While loopen i ifsatserna är för att vänta på att knappen släpps
        if lcd.buttonPressed(lcd.UP):
            while lcd.buttonPressed(lcd.UP):
                pass            
            leds[selected_led].change(1.0)
            lcd.clear()
            lcd.message(leds[selected_led].getStatus())
        elif lcd.buttonPressed(lcd.DOWN):
            while lcd.buttonPressed(lcd.DOWN):
                pass
            leds[selected_led].change(-1.0)
            lcd.clear()
            lcd.message(leds[selected_led].getStatus())
        elif lcd.buttonPressed(lcd.SELECT):
            while lcd.buttonPressed(lcd.SELECT):
                pass
            leds[selected_led].execute()
            lcd.clear()
            lcd.message(leds[selected_led].getStatus())
        elif lcd.buttonPressed(lcd.LEFT):#Ändra lampa att blinka
            while lcd.buttonPressed(lcd.LEFT):
                pass
            selected_led-=1
            if selected_led<0:
                selected_led=number_of_leds-1
            lcd.clear()
            lcd.message(leds[selected_led].getStatus())
        elif lcd.buttonPressed(lcd.RIGHT):#ska skifta mellan att ändra frekvens och dc
            while lcd.buttonPressed(lcd.RIGHT):
                pass
            leds[selected_led].changeFactor()
            lcd.clear()
            lcd.message(leds[selected_led].getStatus())
except KeyboardInterrupt:
        lcd.clear()
        GPIO.cleanup()
