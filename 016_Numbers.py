# ---------------
# -- Numbers --
# ---------------

# Integer

print (type(10))
print (type(100))
print (type(0))
print (type(-10))
print (type(-100))

# Float

print (type(10.76))
print (type(100.99))
print (type(0.87))
print (type(-10.45))
print (type(-0.56))

# Complex

ComplexNumber = 5+6j
print (type(ComplexNumber))
print ("Real part is: {}".format(ComplexNumber.real))
print ("Imaginary part is: {}".format(ComplexNumber.imag))

# You can convert from Int to Float or Complex
# You can convert from Float to Int or Complex
# you can't convert Complex to any type

print (100)
print (float(100))
print (complex(100))

print (10.65)
print (int(10.65))
print (complex(10.65))

print (12+4j)
# print (int(12+4j))   # ==> Error
# print (float(12+4j)) # ==> Error