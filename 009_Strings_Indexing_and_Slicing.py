# ---------------------------------
# -- Strings Indexing & Slicing --
# ---------------------------------

# Indexing (Access Single Item)

a = "I love Python"
print (a [0]) # ==> Index 0 ==> I
print (a [9]) # ==> Index 9 ==> t
print (a [-1]) # ==> First character from the end
print (a [-6]) # ==> Index -6 ==> p

# Slicing (Access multiple Sequence Items)
# [Start:end] [start:end:steps] End not included

print (a [8:11])
print (a [3:5])
print (a [:5]) 
print (a [5:])
print (a [::2])