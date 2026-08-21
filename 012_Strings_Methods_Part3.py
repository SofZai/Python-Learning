# -----------------------
# -- Strings Methods --
# -----------------------

# index()

a = "I love Python"
print (a.index("P")) # ==> index num 7
print (a.index("P",0,10)) # ==> index num 7
#print (a.index("P",0,5)) # ==> Error

# find()

b = "I love python"
print (b.find("p", 0, 5)) # ==> -1

# rjust(width, fill char) ljust(width, fill char)

c = "Sofiane"
print (c.rjust(10, "#"))
print (c.ljust(10, "#"))

# splitlines()

d = """first line
second line
third line"""
print (d.splitlines())

e = "first line\nsecond line\nthird line"
print (e.splitlines())

# expandtabs()

f = "hello\tworld\tI\tlove\tPython"
print (f)
print (f.expandtabs(2))

# ----------------------------------------

g = "I Love Python And 3D"
h = "I Love Python And 3d"
print (g.istitle())
print (h.istitle())

i = " "
print (i.isspace())

j = "i love python and 3d"
k = "I Love Python And 3d"
print (j.islower())
print (k.islower())

l = "sofzai"
m = "sof_zai"
n = "sof--zai"
print(l.isidentifier())
print(m.isidentifier())
print(n.isidentifier())

o = "AaaaaBbbbb"
p = "AaaaaBbbbb1111"
print (o.isalpha())
print (p.isalpha())

q = "AaaaaBbbbb"
r = "AaaaaBbbbb1111"
print (q.isalnum())
print (r.isalnum())