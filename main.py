import time

listy = [[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]]
total = 0

def grid(x,y,z,state):
    listy[int(z)][int(y)][int(x)] = int(state)

def gridfindstate(x,y,z):
    return listy[int(z)][int(y)][int(x)]

def send():
    global total
    total += 1
    string = ''
    for i in range(8):
        string+='z='+str(i)+' '+''.join(str(b) for a in listy[i] for b in a)
    
    print('Grid', str(total)+':')
    print(string.replace('1','1').replace('0','-')+'\n')
    time.sleep(0.01)

# --- CODE GOES BELOW HERE ---

def zero():
    for z in range(8):
        for y in range(8):
            for x in range(8):
                grid(x,y,z,0)

def fill():
    for z in range(8):
        for y in range(8):
            for x in range(8):
                grid(x,y,z,1)

def layerbylayer():
    for z in range(8):
        for y in range(8):
            for x in range(8):
                grid(x,y,z,1)
        
        send() # Has a sleep within it
        
        for j in range(8):
            for i in range(8):
                grid(x,y,z,0)

        send()

def insidethenout():
    zero()
    for i in range(4):
        j = (i+1)*2
        k = 3-i
        for z in range(j):
            for y in range(j):
                for x in range(j):
                    grid(x+k,y+k,z+k,1)
        send()
        if i != 4:
            zero()

def outsidethenin():
    fill()
    for i in range(4):
        j = (3-i)*2
        k = i+1
        for z in range(j):
            for y in range(j):
                for x in range(j):
                    grid(x+k,y+k,z+k,1)
        send()
        if i != 4:
            zero()

def insidethenouthollow():
    zero()
    for i in range(4):
        j = (i+1)*2
        pastj = j-2
        k = 3-i
        pastk = k+1
        for z in range(j):
            for y in range(j):
                for x in range(j):
                    grid(x+k,y+k,z+k,1)
                    
        for z in range(pastj):
            for y in range(pastj):
                for x in range(pastj):
                    grid(x+pastk,y+pastk,z+pastk,0)
        send()
        if i != 3:
            zero()


def outsidetheninhollow():
    zero()
    for i in range(4):
        j = (3-i)*2
        pastj = j-2
        k = i+1
        pastk = k+1
        for z in range(j):
            for y in range(j):
                for x in range(j):
                    grid(x+k,y+k,z+k,1)
        for z in range(pastj):
            for y in range(pastj):
                for x in range(pastj):
                    grid(x+pastk,y+pastk,z+pastk,0)
        send()
        zero()

def fillfrombottom():
    maxi = 0
    for x in range(8):
        for y in range(8):
            for z in range(8):
                if gridfindstate(x,y,z) == 1:
                    maxz = z

            for z2 in range(8):
                if z2 < maxz:
                    grid(x,y,z2,1)
            maxz = 0    

def fillfromtop():
    maxi = 0
    for x in range(8):
        for y in range(8):
            for z in range(8):
                if gridfindstate(x,y,z) == 1:
                    maxz = z

            for z2 in range(8):
                if z2 > maxz:
                    grid(x,y,z2,1)
            maxz = 0


# --- <Visualiser> ---

'''
I want to have the LED Cube light up in response to either the sound coming out or the sound going in.

If it was high then gets lower, make the middle go down first then the outside goes down following
If it stays the same, make them all move to the same point (if its high then all stay high, if its low then all stay low)
If it was low then gets higher, make the middle go up first then the outside goes up following

What other possiblilies are there?
Make a relative point for the pitch (ie the middle is ...Hz (middle), high is ...Hz (top) and low is ...Hz (bottom)) (of cube)

frequences is a list of the frequences at every 0.1s interval or so
'''
class Visualiser(object):
    
    def __init__(self, previousfreq, currentfreq):
        self.previousfreq = previousfreq
        self.currentfreq = currentfreq

    def hightolow(self):

        for i in range(4):
            j = (i+1)*2
            pastj = j-2
            k = 3-i
            pastk = k+1

            for y in range(j):
                for x in range(j):
                    grid(x+k,y+k,0,1)
                        
            for y in range(pastj):
                for x in range(pastj):
                    grid(x+pastk,y+pastk,0,0)
            send()
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

# --- <Fluid> ---

def fluid():
    # Do some cool shit
    x=x

# --- <Fluid/> ---

def run():
    zero()
    Visualiser(0,1).hightolow()

run()

# --- CODE GOES ABOVE HERE ---


'''
USE SHIFT PI MODULE
'''
