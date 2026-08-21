# -------------------
# -- Set Metjods --
# -------------------

# issuperset()
print ("issuperset")

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print (a.issuperset(b))
print (a.issuperset(c))

print ("=" * 40)
# issubset()
print ("issubset")

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}
print (d.issubset(e))
print (d.issubset(f))

print ("=" * 40)
# isdisjoint()
print ("isdisjoint")

g = {1, 2, 3, 4}
h = {1 , 2, 3}
i = {5, 6, 7}
print (g.isdisjoint(h))
print (g.isdisjoint(i))
