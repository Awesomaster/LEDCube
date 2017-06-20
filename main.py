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
        i = 7-i
        string+='z='+str(i)+' '+''.join(str(b) for a in listy[i] for b in a)
    
    print('Grid', str(total)+':')
    print(string.replace('1','1').replace('0','-')+'\n')
    time.sleep(0.01)

# --- CODE GOES BELOW HERE ---

# zero: A function that turns every LED in the array off
def zero():
    for z in range(8):
        for y in range(8):
            for x in range(8):
                grid(x,y,z,0)

# fill: A function that turns on every LED in the array
def fill():
    for z in range(8):
        for y in range(8):
            for x in range(8):
                grid(x,y,z,1)

# layerbylayer: A function that goes from the bottom layer to the top layer and turns them on then off
def layerbylayer():
    for z in range(8):
        for y in range(8):
            for x in range(8):
                grid(x,y,z,1)
        send() # Has a sleep within it
        for j in range(8):
            for i in range(8):
                grid(j,i,z,0)
        send()

# insidethenout: A function that fills the cube from the middle, part by part
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

# outsidethenin: A function that fills the cube then goes from the outside and turns them off part by part
def outsidethenin():
    fill()
    for i in range(5):
        j = (4-i)*2
        k = i
        for z in range(j):
            for y in range(j):
                for x in range(j):
                    grid(x+k,y+k,z+k,1)
        send()
        if i != 4:
            zero()

# insidethenouthollow: A function that goes through each outer layer and turns them on then off from the middle
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

# outsidetheninhollow: A function that goes through each outer layer and turns them on then off from the outside
def outsidetheninhollow():
    zero()
    for i in range(5):
        j = (4-i)*2
        pastj = j-2
        k = i
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

# fillfrombottom: A function that gets every point that is turned on and turns on every LED below it
def fillfrombottom():
    maxz = 0
    for x in range(8):
        for y in range(8):
            for z in range(8):
                if gridfindstate(x,y,z) == 1:
                    maxz = z
            for z2 in range(8):
                if z2 < maxz:
                    grid(x,y,z2,1)
            maxz = 0
    send()

# fillfrombottom: A function that gets every point that is turned on and turns on every LED below it
def fillfromtop():
    for x in range(8):
        x = 7-x
        for y in range(8):
            minz = 7
            y = 7-y
            for z in range(8):
                z = 7-z
                if gridfindstate(x,y,z) == 1:
                    minz = z

            for z2 in range(8):
                z2 = 7-z2
                if z2 > minz:
                    grid(x,y,z2,1)
            minz = 0
    send()

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
    send()
    grid(0,2,4,1)
    grid(2,2,4,1)
    #Visualiser(0,1).hightolow()

run()

# --- CODE GOES ABOVE HERE ---


'''
USE SHIFT PI MODULE
'''
