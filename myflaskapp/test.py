#!/usr/bin/python
def turnOn():
    import RPi.GPIO as GPIO #imports GPIO libraries
    from time import sleep  #imports sleep function
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
 #   print "Relay is turned on" 
    GPIO.setup(11, GPIO.OUT) #sets gpio pin 11 
    GPIO.output(11, 1) # sets GPIO 11 as HIGH (on)
    sleep(1) #pauses the script for 5 seconds.
#    print "Relay is turned off"
    GPIO.output(11, 0) #sets  GPIO 11 as LOW (off)
    GPIO.cleanup() #use this to  restore gpio default values
