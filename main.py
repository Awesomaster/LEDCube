import time
import common
import functions
import music
import fluid

def run():
    functions.zero()
    common.send()
    common.grid(0,2,4,1)
    common.grid(2,2,4,1)
    common.send()
    functions.zero()
    music.Visualiser(0,1).hightolow()

run()

# Refer to listy as common.listy

'''
USE SHIFT PI MODULE
'''
