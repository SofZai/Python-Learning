# -----------------------
# -- Strings Methods --
# -----------------------

# split() rsplit()
a = "I love Python and PHD"
print (a.split())
print (type(a.split()))

b = "I-love-Python-and-PHD"
print (b.split("-"))

c = "I-love-Python-and-PHD"
print (c.split("-", 2))

d = "I-love-Python-and-PHD"
print (d.rsplit("-", 2))

# center()

e = "sofiane"
print (e.center(11)) # spaces
print (e.center(11, "#"))
print (e.center(15, "@"))

# count 

f = "I Love Python and PHP PHP"
print (f.count("PHP"))
print (f.count("PHP", 0, 24))

# swapcase()

g = "I Love Python"
print (g.swapcase())

# startswith()

i = "I Love Python"
print (i.startswith("I"))
print (i.startswith("S"))
print (i.startswith("P", 7,12))

# endswith()

j = "I Love Python"
print (j.endswith("n"))
print (j.endswith("a"))
print (j.endswith("e", 2, 6))