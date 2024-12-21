# Random Module - Pseudorandom number generators need to watch video on khan acadmey

import random
random_integer = random.randit(1, 10)
print("random integer")
# create own module
# random.random () random floating point. [()  to activate the printheces]

# import random

random_integer = random.randint(1, 10)
# print(random_integer)

# Need to learn how to create an own module
# random module - right click - new- python file - named as my_module.py
# my_favourite_number
# import my module
# print(my_favourite_number)

# The following functions generate specific real-valued distributions. 
# Function parameters are named after the corresponding variables in the distribution’s equation, 
# as used in common mathematical practice; most of these equations can be found in any statistics text.

# random.random()
# Return the next random floating-point number in the range 0.0 <= X < 1.0

# random.uniform(a, b)
# Return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

# The end-point value b may or may not be included in the range depending on floating-point 
# rounding in the expression a + (b-a) * random().
# random_number_0_to_1 = random.random()

#Write a programe for Heads and Tails

random_heads_or_tails = random.eandint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")