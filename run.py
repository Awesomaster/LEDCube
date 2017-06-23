import time
import common
import functions
import music
import fluid

# Things from common file

def send():
    common.send()

def grid(x,y,z,state):
    common.grid(x,y,z,state)

# Things from functions file

def zero():
    functions.zero()
    common.send()

def fill():
    functions.fill()

def layerbylayer():
    functions.layerbylayer()

def insidethenout():
    functions.insidethenout()

def outsidethenin():
    functions.outsidethenin()

def insidethenouthollow():
    functions.insidethenouthollow()

def outsidetheninhollow():
    functions.outsidetheninhollow()

def fillfrombottom():
    functions.fillfrombottom()

def fillfromtop():
    functions.fillfromtop()

# Things from music file

def song(frequencies):
    music.song(frequencies)
