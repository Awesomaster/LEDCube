import RPi.GPIO as GPIO
from time import sleep
import common

GPIO.setmode(GPIO.BCM)


# FOR ANGUS:
ser0   = 13    #pin 14 on the shift
ser1   = 16    #pin 14 on the shift
ser2   = 17   #pin 14 on the shift
ser3   = 18   #pin 14 on the shift
ser4   = 19   #pin 14 on the shift
ser5   = 20   #pin 14 on the shift
ser6   = 21   #pin 14 on the shift
ser7   = 22   #pin 14 on the shift
ser8   = 23   #pin 14 on the shift

srclk0 = 4    #pin 11 on the shift
srclk1 = 5   #pin 11 on the shift
srclk2 = 6   #pin 11 on the shift
srclk3 = 7   #pin 11 on the shift
srclk4 = 8   #pin 11 on the shift
srclk5 = 9   #pin 11 on the shift
srclk6 = 10   #pin 11 on the shift
srclk7 = 11   #pin 11 on the shift
srclk8 = 12   #pin 11 on the shift

layerclock  = 2    #pin 12 on the 75HC595
columnclock = 3
##

# FOR JOSH:


##

def setup():
    GPIO.setup(ser0, GPIO.OUT)
    GPIO.setup(ser1, GPIO.OUT)
    GPIO.setup(ser2, GPIO.OUT)
    GPIO.setup(ser3, GPIO.OUT)
    GPIO.setup(ser4, GPIO.OUT)
    GPIO.setup(ser5, GPIO.OUT)
    GPIO.setup(ser6, GPIO.OUT)
    GPIO.setup(ser7, GPIO.OUT)
    GPIO.setup(ser8, GPIO.OUT)

    GPIO.setup(srclk0, GPIO.OUT)
    GPIO.setup(srclk1, GPIO.OUT)
    GPIO.setup(srclk2, GPIO.OUT)
    GPIO.setup(srclk3, GPIO.OUT)
    GPIO.setup(srclk4, GPIO.OUT)
    GPIO.setup(srclk5, GPIO.OUT)
    GPIO.setup(srclk6, GPIO.OUT)
    GPIO.setup(srclk7, GPIO.OUT)
    GPIO.setup(srclk8, GPIO.OUT)

def execute():
    for i in range(8):
        GPIO.output(layerclock, 0)
        GPIO.output(srclk0, 0) # Start looking at the z shift register
        GPIO.output(ser0, 1) # Turn layer on

        # Because they are all different variables I cannot put them in a loop which makes me sad but alas thats how the news goes
        GPIO.output(columnclock, 0)
        for j in range(common.listy[i][0]):
            GPIO.output(srclk1, 0)
            GPIO.output(ser1, int(j))
            GPIO.output(srclk1, 1)
        GPIO.output(columnclock, 1)
        GPIO.output(columnclock, 0)
        for j in range(common.listy[i][1]):
            GPIO.output(srclk2, 0)
            GPIO.output(ser2, int(j))
            GPIO.output(srclk2, 1)
        GPIO.output(columnclock, 1)
        GPIO.output(columnclock, 0)
        for j in range(common.listy[i][2]):
            GPIO.output(srclk3, 0)
            GPIO.output(ser3, int(j))
            GPIO.output(srclk3, 1)
        GPIO.output(columnclock, 1)
        GPIO.output(columnclock, 0)
        for j in range(common.listy[i][3]):
            GPIO.output(srclk4, 0)
            GPIO.output(ser4, int(j))
            GPIO.output(srclk4, 1)
        GPIO.output(columnclock, 1)
        GPIO.output(columnclock, 0)
        for j in range(common.listy[i][4]):
            GPIO.output(srclk5, 0)
            GPIO.output(ser5, int(j))
            GPIO.output(srclk5, 1)
        GPIO.output(columnclock, 1)
        GPIO.output(columnclock, 0)
        for j in range(common.listy[i][5]):
            GPIO.output(srclk6, 0)
            GPIO.output(ser6, int(j))
            GPIO.output(srclk6, 1)
        GPIO.output(columnclock, 1)
        GPIO.output(columnclock, 0)
        for j in range(common.listy[i][6]):
            GPIO.output(srclk7, 0)
            GPIO.output(ser7, int(j))
            GPIO.output(srclk7, 1)
        GPIO.output(columnclock, 1)
        GPIO.output(columnclock, 0)
        for j in range(common.listy[i][7]):
            GPIO.output(srclk8, 0)
            GPIO.output(ser8, int(j))
            GPIO.output(srclk8, 1)
        GPIO.output(columnclock, 1)
        GPIO.output(srclk0, 1) # Switch to next layer

    GPIO.output(layerclock, 1)

setup()
