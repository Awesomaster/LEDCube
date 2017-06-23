# LEDCube
Code for the LEDCube project 2017 engineering studies Yr 12

# All current functions (As of 23rd June 2017)

send() -> Print grid in current state (will be changed to sending to cube)

grid(x,y,z,state) -> sets the LED at position x,y,z to the state (either off (0) or on (1))

zero() -> Turns all LEDs off

fill() -> Turns all LEDs on

layerbylayer() -> Goes from bottom layer to the top layer turning them on then off

insidethenout() -> Fills the cube from the middle out, part by part

insidethenouthollow() -> Fills the cube from the middle out, part by part, hollowing each part

outsidethenin() -> Opposide of insidethenout()

outsidetheninhollow() -> Opposide of insidethenouthollow()

fillfromtop() -> Fills from the top down to every point that is on

fillfrombottom() -> Fills from the bottom up to every point that is on

song(frequencies) -> Frequencies is a range of frequencies at every something rather interval of the song, then takes them and manipulates then to a layer flowing up and down the cube
