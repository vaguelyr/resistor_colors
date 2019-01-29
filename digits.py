# vague
# flashcard style thing for learning resistor codes
# this one does single color = number digits


import time # sleep
import random

# lookup tables 

# bbroygbvgw
colors = [ "black", "brown" , "red"  , "orange"  , "yellow"  , "green"  , "blue"  , "violet"  , "grey"  , "white" ]

digits = [ 0,1,2,3,4,5,6,7,8,9 ]


while True:
    t = random.randrange(10)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(colors[t])
    time.sleep(1.5)
    print(digits[t])
    time.sleep(1)
