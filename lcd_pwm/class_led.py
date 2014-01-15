# -*- coding: cp1252 -*-
import RPi.GPIO as GPIO
class Led:
    def __init__(self,port,frequency=1.0, dc=50, factor=0):
        self.port=port
        self.frequency=frequency
        self.new_frequency=frequency
        self.new_dc=dc
        self.dc=dc
        self.factor=factor#0=frekvens
        GPIO.setup(self.port, GPIO.OUT)
        self.pwm=GPIO.PWM(port,self.frequency)
        self.pwm.start(dc)

    def changeFactor(self):
        self.factor^=1#xor, alternerar vilken faktor som påverkas

    def execute(self):
        if self.factor==0:
            self.changeFrequency()
        else:
            self.changeDC()

    def change(self, change):
        if self.factor==0:
            self.setFrequency(change)
        else:
            self.setDC(change)
    
    def setFrequency(self,change):
        if (self.new_frequency+change)>0:#nya frekvensen måste vara större än noll
            self.new_frequency+=change
        
    def changeFrequency(self):
        self.frequency=self.new_frequency
	self.pwm.ChangeFrequency(self.frequency)

    def setDC(self,change):
	if ((self.new_dc+change)>=0 )& ((self.new_dc+change)<=100):
            self.new_dc+=change
	
    def changeDC(self):
	self.dc=self.new_dc
	self.pwm.ChangeDutyCycle(self.dc)

    def getStatus(self):#returnerar nuvarande status som sträng
        if self.factor==0:
            factor="F"
        else:
            factor="DC"
	status="-F:%0.1f, DC:%d %s\n%dF:%0.1f, DC:%d"%(self.new_frequency, self.new_dc, factor, self.port, self.frequency, self.dc)
        return status
        
