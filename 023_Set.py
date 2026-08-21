# -----------
# -- Set --
# -----------

# Not Ordered and Not Indexed

mySet1 = {"Sofiane", "Kossai", "Mossab"}

print (mySet1)
# print (mySet1[0]) # ==> Error

# Slicing can't be done

mySet2 = {1 ,2 ,3, 4, 5}
# print (mySet2[0:2]) # ==> Error

# Set has only immutable data (Numbers, String, Tuples); List and Dict are not 

# mySet3 = {1, "sofiane", 100.3, True, [1, 2, 3]} # ==> unhashable type: 'list'
mySet3 = {1, "sofiane", 100.3, True, (1, 2, 3)}

print (mySet3)

# Set Items are unique
mySet4 = {1, 1, "one", "sofiane", 1, "one"}
print (mySet4)