# -----------------------
# -- Type Conversion --
# -----------------------

# str()

a = 10
print (type (a))
print (type (str (a)))

print ("=" * 40)

# tuple()

c = "Sofiane"
d = [1, 2, 3, 4, 5]
e = {"A", "B", "C"}
f = {"A" : 1, "B" : 2}

print(tuple (c))
print(tuple (d))
print(tuple (e))
print(tuple (f))

print ("=" * 40)

# list()

g = "Sofiane"
h = (1, 2, 3, 4, 5)
i = {"A", "B", "C"}
j = {"A" : 1, "B" : 2}

print(list (g))
print(list (h))
print(list (i))
print(list (j))

print ("=" * 40)

# set()

k = "Sofiane"
l = (1, 2, 3, 4, 5)
m = ["A", "B", "C"]
n = {"A" : 1, "B" : 2}

print(set (k))
print(set (l))
print(set (m))
print(set (n))

print ("=" * 40)

# dict()

p = (("A", 1), ("B", 2), ("C", 3))
q = [["one", 1], ["two", 2]]

print(dict (p))
print(dict (q))
