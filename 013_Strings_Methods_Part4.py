# -----------------------
# -- Strings Methods --
# -----------------------

# replace(old value, new value, count)

a = "Hello one two three one one"
print (a.replace("one","1"))
print (a.replace("one","1", 1))

# join(iterable)

b = ["sofiane","kossai","mossab"]
print ("-".join(b))
print (" ".join(b))
print (type(" ".join(b)))
