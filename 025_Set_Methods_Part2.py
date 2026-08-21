# -------------------
# -- Set Methods --
# -------------------

# difference ()
print ("difference")

a = {1, 2, 3, 4}
b = {1, 2, "Sofiane", 4}

print (a)
print (a.difference (b)) # ==> a-b
print (a)

print ("=" * 40)

# difference_update()
print ("difference_update")

c = {1, 2, 3, 4}
d = {1, 2, 3, "Sofiane", "Kossai"}
print (c)
c.difference_update(d) # ==> c-d
print (c)

print ("=" * 40)

# intersection()
print ("intersection")

e = {1, 2, 3, 4, "X"}
f = {"Sofiane", "X", 2}
print (e)
print (e.intersection(f)) # ==> e & f
print (e)

print ("=" * 40)

# intersection_update()
print ("intersection_update")

g = {1, 2, 3, 4, "X"}
h = {"Sofiane", "X", 4}
print (g)
g.intersection_update(h) # ==> g & h
print (g)

print ("=" * 40)

# symetric_differnce()
print ("symetric_difference")

i = {1, 2, 3, 4, 5, "Sofiane"}
j = {"Sofiane", "one", 1, 2, 4}
print (i)
print (i.symmetric_difference(j)) # i ^ j
print (i)

print ("=" * 40)

# symetric_differnce_update()
print ("symetric_difference_update")

k = {1, 2, 3, 4, 5, "X"}
l = {"Sofiane", "one", 1, 2, 4}
print (k)
k.symmetric_difference_update(l) # k ^ l
print (k)