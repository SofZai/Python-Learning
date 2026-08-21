# ------------------------------------
# -- Modules ==> Built In Modules --
# ------------------------------------
# [1] Module is a file contain a set of functions
# [2] You can import module in your app to help you
# [3] You can import multiples modules 
# [4] You can create your own module
# [5] modules saves your time
# ------------------------------------

# Import Main Module

# import random
# print (random)
# print (f"Print Random Float Number {random.random ()}") 

# Show All functions inside Module

# import random
# print (dir(random))

# Import one or two functions from module

from random import randint, random

print (f"Print Random Integer {randint (10, 100)}")
print (f"Print Random Float Number {random ()}") 