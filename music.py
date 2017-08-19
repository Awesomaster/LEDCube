import time
import common
import functions
import math
import shifty

# --- <Visualiser> ---

'''
I want to have the LED Cube light up in response to either the sound coming out or the sound going in.

If it was high then gets lower, make the middle go down first then the outside goes down following
If it stays the same, make them all move to the same point (if its high then all stay high, if its low then all stay low)
If it was low then gets higher, make the middle go up first then the outside goes up following

What other possiblilies are there?
Make a relative point for the pitch (ie the middle is ...Hz (middle), high is ...Hz (top) and low is ...Hz (bottom)) (of cube)

Range of frequencies in common songs is 20-4000 Hz
Therefore we will make it each row the log base 2 of the freqencey
frequences is a list of the frequences at every 0.1s interval or so
'''

class Visualiser(object):

    def __init__(self, previousfreq, currentfreq):
        self.previousfreq = previousfreq
        self.currentfreq = currentfreq

    def hightolow(self):
        z = self.currentfreq
        for i in range(6):
            j = (i+1)*2
            pastj = j-2
            pasterj = j-4
            k = 3-i
            pastk = k+1
            pasterk = k+2

            # Turn on the inside circle of a layer
            if j > 10:
                for x in range(8):
                    for y in range(8):
                        common.grid(x,y,z-1,0)
            elif j > 8:
                for x in range(8):
                    for y in range(8):
                        common.grid(x+k,y+k,z,0)
                        common.grid(x+k,y+k,z-1,1)
            else:
                for x in range(j):
                    for y in range(j):
                        common.grid(x+k,y+k,z,1)
                        common.grid(x+k,y+k,z-1,0)

            # Turn off the past inside ring and turn on ring layer of the lower layer
            if j < 10:
                for x in range(pastj):
                    for y in range(pastj):
                        common.grid(x+pastk,y+pastk,z,0)
                        common.grid(x+pastk,y+pastk,z-1,1)

            if pasterj >= 0:
                for x in range(pasterj):
                    for y in range(pasterj):
                        common.grid(x+pasterk,y+pasterk,z-1,0)

            common.send()
            shifty.execute()

    def lowtohigh(self):
        z = self.currentfreq
        for i in range(6):
            j = (i+1)*2
            pastj = j-2
            pasterj = j-4
            k = 3-i
            pastk = k+1
            pasterk = k+2

            # Turn on the inside circle of a layer
            if j > 10:
                for x in range(8):
                    for y in range(8):
                        common.grid(x,y,z+1,0)
            elif j > 8:
                for x in range(8):
                    for y in range(8):
                        common.grid(x+k,y+k,z,0)
                        common.grid(x+k,y+k,z+1,1)
            else:
                for x in range(j):
                    for y in range(j):
                        common.grid(x+k,y+k,z,1)
                        common.grid(x+k,y+k,z+1,0)

            # Turn off the past inside ring and turn on ring layer of the lower layer
            if j < 10:
                for x in range(pastj):
                    for y in range(pastj):
                        common.grid(x+pastk,y+pastk,z,0)
                        common.grid(x+pastk,y+pastk,z+1,1)

            if pasterj >= 0:
                for x in range(pasterj):
                    for y in range(pasterj):
                        common.grid(x+pasterk,y+pasterk,z+1,0)

            common.send()
            shifty.execute()

    def staysame(self):
        z = self.currentfreq

        for x in range(8):
            for y in range(8):
                common.grid(x,y,z,1)

        common.send()
<<<<<<< HEAD

=======
        shifty.execute()
        
>>>>>>> 8fa3278412ee4467a0dd46683473d21b5471afd3
        for x in range(8):
            for y in range(8):
                common.grid(x,y,z,0)

        common.send()
        shifty.execute()

def song(frequencies):
    for i in range(len(frequencies)):

        current = frequencies[i]
        if i == 0:
            previous = current
        else:
            previous = frequencies[i-1]

        current = int((math.log(current, 2)/12)*8)
        previous = int((math.log(previous, 2)/12)*8)
        print(current)

        if current > 7:
            current = 7
        elif current < 0:
            current = 0

        if previous > 7:
            previous = 7
        elif previous < 0:
            previous = 0

        # High to Low
        if current < previous:
            while current < (previous):
                Visualiser(previous, previous-1).hightolow()
                previous-=1

        # Low to High
        if current > previous:
            while current > (previous):
                Visualiser(previous, previous+1).lowtohigh()
                previous+=1

        # Stay Same
        if current == previous:
            Visualiser(previous, current).staysame()

# --- <Visualiser/> ---
