import time
import run
# Run is a file in which I have compiled all the functions that are used and made them subfunctions, as well as making zero send after it runs

def play():
    run.setup()
    run.zero()
    for i in range(50):
        run.layerbylayer()
        time.sleep(1)
play()
