# ---------------------------------------------------
# -- Calculate Age Advenced Version And Training --
# ---------------------------------------------------

# Collact Age DATA 

age = int (input ("Please enter your age: ").strip())

# Collect Time Unit DATA

unit = input ("Please choose Time unit : Months, Weeks, Days ").strip().lower()

# Get Time Units
months = age * 12
weeks = months * 4
days = age *365

if unit == "months" :
    print (f"You lived for {months:,} Months.")
elif unit == "weeks" :
    print (f"You lived for {weeks:,} Weeks.")
elif unit == "days" :
    print (f"You lived for {days:,} Days.")
    