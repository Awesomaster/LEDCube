import time
import common
import functions
import music
import fluid

def run():
    functions.zero()
    common.send()
    current = 4
    previous = 6
    #music.Visualiser(previous,current).hightolow()
    while current < (previous):
        music.Visualiser(previous, current).lowtohigh()
        current+=1

run()

# Refer to listy as common.listy

'''
USE SHIFT PI MODULE
'''
