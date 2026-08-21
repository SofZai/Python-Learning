# -----------------------------------------
# -- Function parameters and arguments --
# -----------------------------------------

a, b, c = "Sofiane", "Kossai", "Mossab"

print (f"Hello {a}")
print (f"Hello {b}")
print (f"Hello {c}")

# def                            ==> function keyword [define]
# say_hello                      ==> function name
# name                           ==> parameter
# print (f"Hello {name}")        ==> task
# Sofiane                        ==> argument

def say_hello (name) :
    print (f"Hello {name}")

say_hello ("Sofiane")
say_hello (a)
say_hello (b)
say_hello (c)

def addition (n1, n2) :
    print (n1 + n2)

addition (100, 23)

def full_name (first, middle, last) :
    print (f"Full name is {first.strip().capitalize()} {middle.strip().capitalize():.1s} {last.strip().capitalize()} ")

full_name ("sofiane", "cherif", "zaibet")