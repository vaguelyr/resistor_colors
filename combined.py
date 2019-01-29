# vague
# flashcard style thing for learning resistor codes
# the others combined


import time # sleep
import random

# lookup tables 

# bbroygbvgw
colors = [ "black", "brown" , "red"  , "orange"  , "yellow"  , "green"  , "blue"  , "violet"  , "grey"  , "white" ]

digits = [ 0,1,2,3,4,5,6,7,8,9 ]


while True:
    if random.randrange(10) > 5:
        c1 = random.randrange(9) + 1 # dont choose black as first color
        c2 = random.randrange(10)
        c3 = random.randrange(10)

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        print(colors[c1] + " " + colors[c2] + " " + colors[c3])
        time.sleep(5)

        print( ((digits[c1] * 10 ) + digits[c2] ) * (10**digits[c3]) )
        time.sleep(2.5)
    else:
        t = random.randrange(10)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(colors[t])
        time.sleep(1.5)
        print(digits[t])
        time.sleep(1)
