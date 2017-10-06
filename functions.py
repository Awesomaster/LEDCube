import common
import time
import shifty

# --- These Functions Work ---

# zero: A function that turns every LED in the array off
def zero():
    common.listy = common.listy_empty

# fill: A function that turns on every LED in the array
def fill():
    common.listy = common.listy_full

# layerbylayer: A function that goes from the bottom layer to the top layer and turns them on then off
def layerbylayer():
    for z in range(8):
        for y in range(8):
            for x in range(8):
                common.grid(x,y,z,1)
        common.send() # Has a sleep within it
        shifty.execute()
        time.sleep(1)
        for j in range(8):
            for i in range(8):
                common.grid(j,i,z,0)
        common.send()
        shifty.execute()
        time.sleep()

# insidethenout: A function that fills the cube from the middle, part by part
def insidethenout():
    zero()
    for i in range(4):
        j = (i+1)*2
        k = 3-i
        for z in range(j):
            for y in range(j):
                for x in range(j):
                    common.grid(x+k,y+k,z+k,1)
        common.send()
        shifty.execute()
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
                    common.grid(x+k,y+k,z+k,1)
        common.send()
        shifty.execute()
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
                    common.grid(x+k,y+k,z+k,1)

        for z in range(pastj):
            for y in range(pastj):
                for x in range(pastj):
                    common.grid(x+pastk,y+pastk,z+pastk,0)
        common.send()
        shifty.execute()
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
                    common.grid(x+k,y+k,z+k,1)
        for z in range(pastj):
            for y in range(pastj):
                for x in range(pastj):
                    common.grid(x+pastk,y+pastk,z+pastk,0)
        common.send()
        shifty.execute()
        zero()

# fillfrombottom: A function that gets every point that is turned on and turns on every LED below it
def fillfrombottom():
    maxz = 0
    for x in range(8):
        for y in range(8):
            for z in range(8):
                if common.gridfindstate(x,y,z) == 1:
                    maxz = z
            for z2 in range(8):
                if z2 < maxz:
                    common.grid(x,y,z2,1)
            maxz = 0
    common.send()
    shifty.execute()

# fillfromtop: A function that gets every point that is turned on and turns on every LED below it
def fillfromtop():
    for x in range(8):
        x = 7-x
        for y in range(8):
            minz = 7
            y = 7-y
            for z in range(8):
                z = 7-z
                if common.gridfindstate(x,y,z) == 1:
                    minz = z

            for z2 in range(8):
                z2 = 7-z2
                if z2 > minz:
                    common.grid(x,y,z2,1)
            minz = 0
    common.send()
    shifty.execute()
