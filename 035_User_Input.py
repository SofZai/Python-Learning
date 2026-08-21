# ------------------
# -- User Input --
# ------------------

fName = input ("What's your first name?")
lName = input ("what's your last name?")

fName = fName.strip().capitalize()
lName = lName.strip().capitalize()

print (f"Hello {fName:.1s} {lName}; Happy to see you")