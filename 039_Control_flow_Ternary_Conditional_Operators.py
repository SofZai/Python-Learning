# -----------------------------------
# -- Terary Conditional Operator --
# -----------------------------------

country = "Algeria"

if country == "Algeria" : print (f"the weather in {country} is 15.")
elif country == "KSA" : print (f"the weather in {country} is 20.")
else : print (f"{country} in not in the list.")
    
    

# Short if

movieRate = 18
age = 19

if age < movieRate :
    print ("Movie is not goor for you")
else :
    print ("Movie is good for you")

print ("Movie is not good for you " if age < movieRate else "Movie is good for you")