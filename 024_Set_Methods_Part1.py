# -------------------
# -- Set Methods --
# -------------------

# clear()

a = {1, 2, 3}
a.clear ()
print (a)

# union ()

b = {"one", "two", "three"}
c = {1, 2, 3}
d = {"A", "B", 3}

print (b | c | d)
print (b.union (c, d))

# add ()

e ={1, 2, 3, 4}
e.add (5)
e.add (6)
print (e)
print (type (e))

# copy ()

f = {1, 2, 3, 4}
g = f.copy ()

f.add (5)

print (f)
print (g)

# remove ()

h = {1, 2, 3, 4}
h.remove (1)
# h.remove (7) # ==> Error
print (h)

# discard ()

i = {1, 2, 3, 4}
i.discard (1)
i.discard (7)
print (i)

# pop ()

j = {1, 2, 3, True, "sofiane"}
print (j.pop ())

# apdate ()

k = {1, 2, 3}
l = {1, "A", "B"}
k.update (["sof", "kos", 7])
k.update (l)
print (k)

