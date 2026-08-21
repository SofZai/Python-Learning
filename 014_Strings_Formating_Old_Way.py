# -------------------------
# -- Strings Formatting --
# -------------------------

name = "sofiane" ; age = 31 ; rank = 10
print ("My Name Is: " + name)
# print ("My Name Is: " + name + "And My Age Is: " + age) # ==> type error

print ("My Name Is: %s" % "sofiane")
print ("My Name Is: %s" % name)
print ("My Name Is: %s And My Age Is: %d And My Rank Is: %f" % (name, age, rank))
print(type("My Name Is: %s And My Age Is: %d And My Rank Is: %f" % (name, age, rank)))

# %s ==> str ; %d ==> num ; %f ==> float

# control floating point number

a = 10
print ("My number is %.2f" % a)

# Truncate string

b = "hello world"
print ("message is: %s" % b)
print ("message is: %.5s" % b)