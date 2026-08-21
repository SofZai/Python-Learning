# ---------------------------------------------------
# -- Function packing, unpacking arguments *args --
# ---------------------------------------------------

# print (1, 2, 3, 4)
# myList = [1, 2, 3, 4]
# print (myList)
# print (*myList)

def say_hello (*peoples) :
    
    for name in peoples :
        print (f"hello {name}")

say_hello ("Sofiane", "Kossai", "Mossab")

def show_details (name, *skills) :
    print (f"Hello {name} your skills are: ")
    for skill in skills :
        print (skill)

show_details ("Sofiane", "Html", "CSS")

