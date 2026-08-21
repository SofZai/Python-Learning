# --------------------------
# -- Dictionary Methods --
# --------------------------

# clear()
print ("*** Clear ***")

user = {
    "name" : "Sofiane"
}

print (user)
user.clear()
print (user)

print ("=" * 40)

# update()
print ("*** Update ***")

me = {
    "name" : "Sofiane"
}
print (me)
me["age"] = 31
print (me)
me.update({"country" : "Algeria"})
print (me)

print ("=" * 40)

# copy()
print ("*** Copy ***")

a = {
    "name" : "Sofiane"
}
b = a.copy()
print (b)
a.update ({"age" : 31})
print (b)

print ("=" * 40)

# keys() + values()
print ("*** keys + values ***")

print (a.keys())
print (a.values())
