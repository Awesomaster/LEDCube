import RPi.GPIO as GPIO
from time import sleep
import common

GPIO.setmode(GPIO.BCM)


HIGH = 1
LOW  = 0

_SER_pin   = 25    #pin 14 on the 75HC595
_RCLK_pin  = 24    #pin 12 on the 75HC595
_SRCLK_pin = 23   #pin 11 on the 75HC595

def flatten(listy, listx):
    for number in listy:
        if isinstance(number, (list, tuple)):           
            flatten(number, listx)
        else:
            listx.append(number)
            
    return listx

_registers = flatten(common.listy, [])
print(_registers)

_number_of_shiftregisters = 9
all_pins = 72

def pinsSetup(**kwargs):
    global _SER_pin, _RCLK_pin, _SRCLK_pin

    custompins = 0
    serpin = _SER_pin
    rclkpin = _RCLK_pin
    srclkpin = _SRCLK_pin

    if len(kwargs) > 0:
        custompins = 1

        _SER_pin = kwargs.get('ser', _SER_pin)
        _RCLK_pin = kwargs.get('rclk', _RCLK_pin)
        _SRCLK_pin = kwargs.get('srclk', _SRCLK_pin)

    if custompins:
        if _SER_pin != serpin or _RCLK_pin != rclkpin or _SRCLK_pin != srclkpin:
            GPIO.setwarnings(True)
    else:
        GPIO.setwarnings(False)

    GPIO.setup(_SER_pin, GPIO.OUT)
    GPIO.setup(_RCLK_pin, GPIO.OUT)
    GPIO.setup(_SRCLK_pin, GPIO.OUT)

def execute():
    GPIO.output(_RCLK_pin, GPIO.LOW)

    for pin in range(all_pins-1, -1, -1):
        GPIO.output(_SRCLK_pin, GPIO.LOW)

        pin_mode = _registers[pin]

        GPIO.output(_SER_pin, pin_mode)
        GPIO.output(_SRCLK_pin, GPIO.HIGH)

    GPIO.output(_RCLK_pin, GPIO.HIGH)

pinsSetup()
