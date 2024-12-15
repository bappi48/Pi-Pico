from machine import Pin
import utime

trigger = Pin(1, Pin.OUT)
echo = Pin(0, Pin.IN)



def ultra():
    trigger.low()
    utime.sleep_us(2)
    
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    signaloff = 0
    signalon = 0
    
    while echo.value() == 0:
       signaloff = utime.ticks_us()
       
    while echo.value() == 1:
        signalon = utime.ticks_us()
        
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ", distance,"cm")
    
while True:
    ultra()
    utime.sleep(1)
    
    