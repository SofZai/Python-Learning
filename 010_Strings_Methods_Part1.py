# -----------------------
# -- Strings Methods --
# -----------------------

a = "I Love Python"
print (len(a))  # length of 'a' ==> 13 characters

# strip() rstrip() lstrip()
b = "     I love python     "
print (b.strip())
print (len(b.strip()))
print (b.rstrip())
print (len(b.rstrip()))
print (b.lstrip())
print (len(b.lstrip()))

c = "#####I love python#####"
print (c.strip("#"))

d = "#@#@#@I love python@#@#@#"
print (d.strip("@#"))

# title()
e = "I love 2d Graphics and 3d tech and Python"
print (e.title())

# capitalize()
f = "I Love 2d Graphics And 3d tech and Python"
print (f.capitalize())

# zfill

g, h, i = "1", "11", "111"
print (g)
print (h)
print (i)

print (g.zfill(3))
print (h.zfill(3))
print (i.zfill(3))

# upper()
j = "sofiane"
print (j.upper())

# lower
k = "SOFIANE"
print (k.lower())
