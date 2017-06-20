import time
import common
import functions

# --- <Visualiser> ---

'''
I want to have the LED Cube light up in response to either the sound coming out or the sound going in.

If it was high then gets lower, make the middle go down first then the outside goes down following
If it stays the same, make them all move to the same point (if its high then all stay high, if its low then all stay low)
If it was low then gets higher, make the middle go up first then the outside goes up following

What other possiblilies are there?
Make a relative point for the pitch (ie the middle is ...Hz (middle), high is ...Hz (top) and low is ...Hz (bottom)) (of cube)

Range of frequencies in common songs is 20-16000 Hz
frequences is a list of the frequences at every 0.1s interval or so
'''
class Visualiser(object):
    
    def __init__(self, previousfreq, currentfreq):
        self.previousfreq = previousfreq
        self.currentfreq = currentfreq

    def hightolow(self):
        z = 0
        for i in range(4):
            j = (i+1)*2
            pastj = j-2
            k = 3-i
            pastk = k+1

            for y in range(j):
                for x in range(j):
                    common.grid(x+k,y+k,z,1)
                        
            for y in range(pastj):
                for x in range(pastj):
                    common.grid(x+pastk,y+pastk,z,0)
            common.send()
        x=x

    def lowtohigh(self):
        #do b
        x=x

    def staysame(self):
        #do c
        x=x

def song(frequencies):
    for i in range(len(frequencies)):
        
        current = frequencies[i]
        if i == 0:
            previous = current
        else:
            previous = frequencies[i-1]

        # Low To High
        if current > previous:
            Visualiser(previous, current).lowtohigh()

        # High To Low
        if current < previous:
            Visualiser(previous, current).hightolow()

        # Stay Same
        if current == previous:
            Visualiser(previous, current).staysame()

# --- <Visualiser/> ---
