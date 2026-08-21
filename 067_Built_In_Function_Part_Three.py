# -------------------------
# -- Built in function --
# -------------------------
# abs ()
# pow ()
# min ()
# max ()
# slice ()
# -------------------------

# abs ()
print (abs (-19))

# pow (base, exp, mod)

print (pow (2, 3))
print (pow (2, 5, 10))  # ==> (2 ** 5) % 10

# min () , max ()

myNumbers = (1, 23, -4, -34)

print (min (3, 43, -9))
print (max (3, 43, -9))
print (min ("w", "sof", "z"))
print (max ("w", "sof", "z"))
print (min (myNumbers))
print (max (myNumbers))

# slice (start, end, step)

a = ["A", "B", "C", "D", "E", "F"]
print (a [:5])
print (a [slice (5)])
print (a [slice (2, 5)])