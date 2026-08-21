# ----------------------------
# -- Membership Operators --
# ----------------------------
# in
# not in 
# ----------------------------

# string

name = "Sofiane"
print ("S" in name)

print ("=" * 40)

# list

friends = ["Ahmed", "Ali", "Mohamed"]
print ("Ali" in friends)
print ("sofiane" not in friends)

print ("=" * 40)

# Using in and not in with condition

countrisOne = ["Algeria", "KSA", "Egypt"]
countrisOneDiscount = 80

countrisTwo = ["USA", "Italy"]
countrisTwoDiscount = 50

myCountry = "Algeria"

if myCountry in countrisOne :
    print (f"you have an discount of $ {countrisOneDiscount}")
elif myCountry in countrisTwo :
    print (f"you have an discount of ${countrisTwoDiscount}")
else :
    print ("You have not an discount")
