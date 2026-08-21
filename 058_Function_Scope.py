# ----------------------
# -- Function scope --
# ----------------------

# x = 1       # ==> Global scope

def one () :
    global x

    x = 2
    print (f"variable from function scope {x}")

def two () :

    x = 4 
    print (f"variable from function two scope {x}")

one ()
print (f"variable from global scope {x}")
two ()