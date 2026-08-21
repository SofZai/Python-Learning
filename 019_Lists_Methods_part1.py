# ---------------------
# -- Lists Methods --
# ---------------------

# Append ()

MyChildren = ["Kossai", "Mossab"]
MyBrothers = ["Fares", "Riadh"]

MyChildren.append("Djouairia")

MyChildren.append(MyBrothers)

print (MyChildren)
print (MyChildren[3])
print (MyChildren[3][1])

# extend

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["one", "two"]

a.extend(b)
a.extend(c)

print (a)

# remove

d = [1, 2, 3, 4, 5, "sofiane", True, "sofiane", "sofiane"]
d.remove ("sofiane")
print (d)

# sort()

e = [1, 2, 100, 45, -2]
e.sort()
print (e)
e.sort(reverse=True)
print(e)
e.sort(reverse=False)
print (e)

# revers()

f = [10, 1, 34, -5, "ASO", True]
f.reverse()
print (f)
