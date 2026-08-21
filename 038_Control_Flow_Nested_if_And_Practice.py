# -----------------
# -- Nested IF --
# -----------------

name = "Sofiane"
isstudent = "yes"
country = "Algeria"
price = 100

if country == "Algeria" :

    if isstudent == "yes" :
        print (f"price is ${price - 50}")
    else :
        print (f"price is ${price - 30}")

elif country == "KSA" :
    print (f"Price is ${price - 20}")
else :
    print (f"price is ${price - 10}")