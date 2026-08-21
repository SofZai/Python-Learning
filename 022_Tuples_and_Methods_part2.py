# -------------
# -- Tuple -- 
# -------------

# Tuple With One Element

myTuple1 = ("sofiane",)
myTuple2 = "sofiane",

print (type(myTuple1))
print (type(myTuple2))

print (len(myTuple1))
print (len(myTuple2))

# Tuple Concatination

a = (1, 2, 3, 4, 5)
b = (5, 6)

c = a + b
d = a + ("A", True) + b

print (c)
print (d)

# Tuple, List, String Repeat (*)

myString = "Sofiane"
myList = [1, 2]
myTuple = ("A", "B")

print (myString * 3)
print (myList * 3)
print (myTuple * 3)

# Methods ==> count()

e = (1, 2, 4, 4, 3, 4)
print (e.count(4))

# Methods ==> index()

f = (1, 2, 3, 4, 3, 2, 8)
print (f.index(3))

# Tuple Destruct

g = ("A", "B", 4, "C")
x, y, _, z = g

print (x)
print (y)
print (z)