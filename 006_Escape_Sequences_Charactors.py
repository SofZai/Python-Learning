# ---------------------------------- 
# Escape Sequences Characters
# ----------------------------------
# \b ==> back space
print ("hello\bworld") # remove "o"
#
# \new line ==> Escape new line
print ("hello \
world") # remove new line + \
#
# \\ ==> Escape \
print ("I love back slash \\") # ==> Escape \ and print it
#
# \' or \" ==> Escape Quote ' or "
print ('hello \'test\'')
print ("hello \"test\"")
#
# \n ==> Line Feed
print (" hello \n i love python")
#
#\r ==> Carriage Return
print ("123456\rabcd") # ==> print abcd at the place of 1234
#
# \t ==> Horizontal Tab
print ("hello\tpython")
#
# \xxh ==> Character Hex Value
print ("\x73") 