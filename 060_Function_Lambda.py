# ---------------------------
# -- Function ==> lambda --
# -- Anonymous Function  --
# ---------------------------
# [1] It hasn't a name
# [2] You cal call it inline without defining it
# [3] You can use it in return data from another function
# [4] Lambda used for simple functions and def handle the large tasks
# [5] Lambda is one single expression not block of codes
# [6] Lambda type is function
# ---------------------------

def say_hello (name) :
    return f"Hello {name}"

hello = lambda name : f"Hello {name}"

print (say_hello ("Sofiane"))
print (hello ("Kossai"))

print (say_hello.__name__)
print (hello.__name__)

print (type (hello))