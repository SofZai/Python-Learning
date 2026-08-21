# ---------------------
# -- File handling --
# ---------------------
# "a" Append    Open file for appending values, create file if not exists
# "r" Read      [Default value] open file for read and give error if file is not exists
# "w" Write     Open file for writing, create file if not exists
# "x" create    Create file, give error if file exists
# ---------------------  

import os

print (os.getcwd ())

# print (os.path.dirname (os.path.abspath (__file__)))

# print (os.path.abspath (__file__))

file = open(r"C:\Users\CyberTec\Documents\Python\Osama_ELZIRO\Sofiane.txt")