

# 4:simulate single rolling a dice a million times and determine the p
# probability of getting 3 or 6 on top face.(Answer should also be verified
# analitically)


import numpy as np
from random import randint
import random
odds=0
evens=0
trials=1000000
p=0.0

rolling=int(input("How many dise are you going to throw ?: "))
for j in range(rolling):
    result = random.randint(0,5)
        
    #print result
    if result == 0:
        #print "Heads"
        evens += 1
    else:
        #print "Tails"
        odds += 1
    
print ("The result is: ")
print ("Evens: ",evens)
print ("Odds: ",odds)
