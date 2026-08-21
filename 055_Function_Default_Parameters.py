# -----------------------------------
# -- Function default parameters --
# -----------------------------------

def say_hello (name, age, country = "Unknown") :
    print (f"Hello {name} your age is {age} and your country is {country}")

say_hello ("Sofiane", 31, "Algeria")
say_hello ("Sofiane", 31)

