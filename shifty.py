import RPi.GPIO as GPIO
from time import sleep
import common

GPIO.setmode(GPIO.BCM)


HIGH = 1
LOW  = 0

# FOR ANGUS:
_SER0_pin   = 10    #pin 14 on the shift
_SRCLK0_pin = 23   #pin 11 on the shift
_SER1_pin   = 2    #pin 14 on the shift
_SRCLK1_pin = 11   #pin 11 on the shift
_SER2_pin   = 3    #pin 14 on the shift
_SRCLK2_pin = 12   #pin 11 on the shift
_SER3_pin   = 4    #pin 14 on the shift
_SRCLK3_pin = 13   #pin 11 on the shift
_SER4_pin   = 5    #pin 14 on the shift
_SRCLK4_pin = 16   #pin 11 on the shift
_SER5_pin   = 6    #pin 14 on the shift
_SRCLK5_pin = 17   #pin 11 on the shift
_SER6_pin   = 7    #pin 14 on the shift
_SRCLK6_pin = 18   #pin 11 on the shift
_SER7_pin   = 8    #pin 14 on the shift
_SRCLK7_pin = 19   #pin 11 on the shift
_SER8_pin   = 9    #pin 14 on the shift
_SRCLK8_pin = 20   #pin 11 on the shift

_RCLK_pin  = 21    #pin 12 on the 75HC595
##

# FOR JOSH:


##


'''
def flatten(listy, listx):
    for number in listy:
        if isinstance(number, (list, tuple)):           
            flatten(number, listx)
        else:
            listx.append(number)
            
    return listx

registers = flatten(common.listy, [])
print(registers)


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
'''
def setup():
    GPIO.setup(_RCLK_pin, GPIO.OUT)
    GPIO.setup(_SER0_pin, GPIO.OUT)
    GPIO.setup(_SRCLK0_pin, GPIO.OUT)
    GPIO.setup(_SER1_pin, GPIO.OUT)
    GPIO.setup(_SRCLK1_pin, GPIO.OUT)
    GPIO.setup(_SER2_pin, GPIO.OUT)
    GPIO.setup(_SRCLK2_pin, GPIO.OUT)
    GPIO.setup(_SER3_pin, GPIO.OUT)
    GPIO.setup(_SRCLK3_pin, GPIO.OUT)
    GPIO.setup(_SER4_pin, GPIO.OUT)
    GPIO.setup(_SRCLK4_pin, GPIO.OUT)
    GPIO.setup(_SER5_pin, GPIO.OUT)
    GPIO.setup(_SRCLK5_pin, GPIO.OUT)
    GPIO.setup(_SER6_pin, GPIO.OUT)
    GPIO.setup(_SRCLK6_pin, GPIO.OUT)
    GPIO.setup(_SER7_pin, GPIO.OUT)
    GPIO.setup(_SRCLK7_pin, GPIO.OUT)
    GPIO.setup(_SER8_pin, GPIO.OUT)
    GPIO.setup(_SRCLK8_pin, GPIO.OUT)

def execute():
    for i in range(8):
        GPIO.output(_RCLK_pin, GPIO.LOW)
        GPIO.output(_SRCLK0_pin, GPIO.LOW) # Start looking at the z shift register
        GPIO.output(_SER0_pin, GPIO.HIGH) # Turn layer on
        
        # Because they are all different variables I cannot put them in a loop which makes me sad but alas thats how the news goes
        
        for j in range(common.listy[i][0]):
            GPIO.output(_SRCLK1_pin, GPIO.LOW)
            GPIO.output(_SER1_pin, int(j))
            GPIO.output(_SRCLK1_pin, GPIO.HIGH)
        
        for j in range(common.listy[i][1]):
            GPIO.output(_SRCLK2_pin, GPIO.LOW)
            GPIO.output(_SER2_pin, int(j))
            GPIO.output(_SRCLK2_pin, GPIO.HIGH)
        
        for j in range(common.listy[i][2]):
            GPIO.output(_SRCLK3_pin, GPIO.LOW)
            GPIO.output(_SER3_pin, int(j))
            GPIO.output(_SRCLK3_pin, GPIO.HIGH)
        
        for j in range(common.listy[i][3]):
            GPIO.output(_SRCLK4_pin, GPIO.LOW)
            GPIO.output(_SER4_pin, int(j))
            GPIO.output(_SRCLK4_pin, GPIO.HIGH)
            
        for j in range(common.listy[i][4]):
            GPIO.output(_SRCLK5_pin, GPIO.LOW)
            GPIO.output(_SER5_pin, int(j))
            GPIO.output(_SRCLK5_pin, GPIO.HIGH)
        
        for j in range(common.listy[i][5]):
            GPIO.output(_SRCLK6_pin, GPIO.LOW)
            GPIO.output(_SER6_pin, int(j))
            GPIO.output(_SRCLK6_pin, GPIO.HIGH)
        
        for j in range(common.listy[i][6]):
            GPIO.output(_SRCLK7_pin, GPIO.LOW)
            GPIO.output(_SER7_pin, int(j))
            GPIO.output(_SRCLK7_pin, GPIO.HIGH)
        
        for j in range(common.listy[i][7]):
            GPIO.output(_SRCLK8_pin, GPIO.LOW)
            GPIO.output(_SER8_pin, int(j))
            GPIO.output(_SRCLK8_pin, GPIO.HIGH)
        
        GPIO.output(_SRCLK0_pin, GPIO.HIGH) # Switch to next layer

    GPIO.output(_RCLK_pin, GPIO.HIGH)

setup()
