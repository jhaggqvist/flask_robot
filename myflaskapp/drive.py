
#!/usr/bin/python
import RPi.GPIO as GPIO #imports gpio library
from time import sleep #imports the sleep function from time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.output(7, 0)
GPIO.output(11, 0)
GPIO.output(13, 0)
GPIO.output(15, 0)


def setup():
    import RPi.GPIO as GPIO #imports gpio library
    from time import sleep #imports the sleep function from time library
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(7, 0)
    GPIO.output(11, 0)
    GPIO.output(13, 0)
    GPIO.output(15, 0)

def moveForward():
    setup()
    GPIO.output(11, 1)
    GPIO.output(15, 1)
    sleep(2)
    GPIO.output(11, 0)
    GPIO.output(15, 0)

def moveBackward():
    setup()
    GPIO.output(7, 1)
    GPIO.output(13, 1)
    sleep(2)
    GPIO.output(7, 0)
    GPIO.output(13, 0)

def moveLeft():
    setup()
    GPIO.output(7, 1)
    GPIO.output(15, 1)
    sleep(1)
    GPIO.output(7, 0)
    GPIO.output(15, 0)

def moveRight():
    setup()
    GPIO.output(11, 1)
    GPIO.output(13, 1)
    sleep(1)
    GPIO.output(11, 0)
    GPIO.output(13, 0)
