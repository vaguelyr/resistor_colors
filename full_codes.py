# vague
# flashcard style thing for learning resistor codes
# this one does the full codes. 


import time # sleep
import random

# lookup tables 

# bbroygbvgw
colors = [ "black", "brown" , "red"  , "orange"  , "yellow"  , "green"  , "blue"  , "violet"  , "grey"  , "white" ]

digits = [ 0,1,2,3,4,5,6,7,8,9 ]


while True:
    c1 = random.randrange(9) + 1 # dont choose black as first color
    c2 = random.randrange(10)
    c3 = random.randrange(10)

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    print(colors[c1])
    print(colors[c2])
    print(colors[c3])
    time.sleep(5)

    print( ((digits[c1] * 10 ) + digits[c2] ) * (10**digits[c3]) )
    time.sleep(2.5)
