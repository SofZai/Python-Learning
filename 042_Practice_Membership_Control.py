# -----------------------------------
# -- Practice Membership Control --
# -----------------------------------

admins = ["Sofiane", "Asma", "Kossai", "Mossab"]

name = input ("Please enter your name: ").strip().capitalize()

if name in admins :
    print (f"Welcom {name}")
    option = input ("You are an admin, do you wont update your name or delette it ? ").strip().capitalize()

    # Update option
    if option == "Update" or option == "U" : 
        newName = input ("Please enter your new name: ").strip().capitalize()
        admins [admins.index (name)] = newName
        print ("Name updated")
        print (admins)
    
    # Delatte option
    elif option == "Delatte" or option == "D" :
        admins.remove(name)
        print ("Name deletted !!")
        print (admins)
    
    # Wrong option
    else :
        print ("Wrong choose")

else :
    print (f"Welcom {name}")
    option = input ("You are not an admin, do you wont to add you ? ").strip().capitalize()

    # Add name 
    if option == "Yes" or option == "Y" :
        admins.append (name)

        print (f"Welcom {name} in admins")
        print (admins)

    # Don't add 
    else :
        print (f"good luck {name}")
