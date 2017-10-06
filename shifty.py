import RPi.GPIO as gpio
from time import sleep
import common

gpio.setmode(gpio.BCM)


<<<<<<< HEAD
high = 1
low  = 0

# FOR ANGUS:
ser0   = 13    #pin 14 on layer shift
srclk0 = 4    #pin 11 on layer shift
ser1   = 16    #pin 14 on column shift
srclk1 = 5   #pin 11 on column shift

ser0rclk  = 2    #pin 12 on layer shift
ser1rclk = 3    #pin 12 on column shift
=======
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
>>>>>>> 18bed73c78645cfe5617cbce11365689863839d2
##

# FOR JOSH:


##

<<<<<<< HEAD

def flatten(listy, listx):
    for number in listy:
        if isinstance(number, (list, tuple)):
            flatten(number, listx)
        else:
            listx.append(number)

    return listx

registers = flatten(common.listy, [])
print(registers)

def setup():
    gpio.setup(_RCLK_pin, gpio.OUT)
    gpio.setup(ser0, gpio.OUT)
    gpio.setup(srclk0, gpio.OUT)
    gpio.setup(ser1, gpio.OUT)
    gpio.setup(srclk1, gpio.OUT)
    gpio.setup(ser0rclk, gpio.OUT)
    gpio.setup(ser1rclk, gpio.OUT)

def execute():
    for i in range(8):
        gpio.output(ser0rclk, gpio.low)
        gpio.output(srclk0, gpio.low) # Start looking at the z shift register
        gpio.output(ser0, gpio.high) # Turn layer on

        gpio.output(ser1rclk, gpio.low)
        for j in range(64):
            gpio.output(srclk1, gpio.low)
            gpio.output(ser1, int(registers[j]))
            gpio.output(srclk1, gpio.high)

        gpio.output(ser1rclk, gpio.high)
        gpio.output(ser1rclk, gpio.low)

        gpio.output(srclk0, gpio.high) # Switch to next layer
        gpio.output(srclk0, gpio.low)

    gpio.output(ser0rclk, gpio.high) # turn everything on
    #gpio.output(ser0rclk, gpio.low)
=======
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
>>>>>>> 18bed73c78645cfe5617cbce11365689863839d2

setup()
