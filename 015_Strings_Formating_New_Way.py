# -------------------------
# -- Strings Formatting --
# -------------------------

name = "sofiane"
age = 31
rank = 10
print ("My Name Is: " + name)
# print ("My Name Is: " + name + "And My Age Is: " + age) # ==> type error

print ("My Name Is: {}".format("sofiane"))
print ("My Name Is: {}".format(name))
print ("My Name Is: {:s} And My Age Is: {:d} And My Rank Is: {:f}".format(name, age, rank))
#print(type("My Name Is: {} And My Age Is: {} And My Rank Is: {}".format(name, age, rank)))

# {:s} ==> str ; {:d} ==> num ; {:f} ==> float

# control floating point number

a = 10
print ("My number is {:.2f}".format(a))

# Truncate string

b = "hello world"
print ("message is: {}".format(b))
print ("message is: {:.5s}".format(b))

# Format Money

c = 500162350198
print ("My Money is: {}".format(c))
print ("My Money is: {:,d}".format(c))

# Rearrange items

d, e, f = "one", "two", "three"
print ("Hello {} {} {}".format(d, e, f))
print ("Hello {1} {2} {0}".format(d, e, f)) # 1: index of e ... ==> Hello two three one 
print ("Hello {2} {2} {0}".format(d, e, f))

g, h, i = 10, 20, 30
print ("Hello {} {} {}".format(g, h, i))
print ("Hello {1} {2} {0}".format(g, h, i)) 
print ("Hello {2:d} {2:f} {0:.2f}".format(g, h, i))

# Format in version 3.6+

MyName = "Sofiane"
MyAge = 31
print ("My name is: {MyName} and My Age is {MyAge}")
print (f"My Name is: {MyName} and My Age is: {MyAge}")