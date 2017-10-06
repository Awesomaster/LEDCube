import RPi.GPIO as gpio
from time import sleep
import common

gpio.setmode(gpio.BCM)


high = 1
low  = 0

# FOR ANGUS:
ser0   = 21    #pin 14 on layer shift
srclk0 = 20    #pin 11 on layer shift
ser0rclk  = 16    #pin 12 on layer shift

ser1   = 26    #pin 14 on column shift
srclk1 = 19   #pin 11 on column shift
ser1rclk = 13    #pin 12 on column shift
##

# FOR JOSH:


##


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

setup()
