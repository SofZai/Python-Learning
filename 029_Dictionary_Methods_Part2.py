# --------------------------
# -- Dictionary Methods --
# -------------------------

# setdefault()
print ("*** setdefault ***")

user = {
    "name" : "Sofiane"
}

print (user)
print (user.setdefault("name", "Kossai"))
print (user)

print ("=" * 40)

# popitem()
print ("*** popitem ***")

member = {
    "name" : "sofiane",
    "skill" : "PY"
}

print (member)
member.update({"age" : 31})
print (member.popitem())

print ("=" * 40)

# item()
print ("*** item ***")

view = {
    "name" : "Sofiane",
    "Skill" : "Xbox"
}

allitems = view.items()
print (view)
view.update({"age" : 31})
print (allitems)

print ("=" * 40)

# fromkeys()
print ("*** fromkeys ***")

a = ("One", "Two", "Three")
b = "X"
c = dict.fromkeys (a, b)
print (dict.fromkeys(a, b))
print (c)