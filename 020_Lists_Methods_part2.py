# ---------------------
# -- Lists Methods --
# ---------------------

# clear()

a = [1, 2 ,3, 4]
a.clear()
print (a)

# copy()

b =[1, 2, 3, 4]
c = b.copy()
print (b)
print (c)

b.append(5)
print (b)
print (c)

# count()

d = [1, 2, 3, 4, 3, 3, 2, 5, 9, 2]
print (d.count(3))

# index()

e = ["sofiane", "kossai", "mossab", "kossai", "sofiane"]
print (e.index("kossai"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert (-1,"test")
print (f)

# pop()

g = [1, 2, 3, 4, 5]
print (g.pop(-1))