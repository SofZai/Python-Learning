# --------------------------------------
# -- Date and time ==> Introduction --
# --------------------------------------

import datetime
# print (dir (datetime))
# print (dir (datetime.datetime))

# print the current date and time

print (datetime.datetime.now())

print ("#" * 50)

# print the current year
print (datetime.datetime.now().year)

print ("#" * 50)

# print the current month
print (datetime.datetime.now().month)

print ("#" * 50)

# print the current day
print (datetime.datetime.now().day)

print ("#" * 50)

# print start and end of date
print (datetime.datetime.min)
print (datetime.datetime.max)

print ("#" * 50)
print (datetime.datetime(1994, 3, 29))
print (datetime.datetime(1994, 3, 29, 23, 59, 44))

birthDay = datetime.datetime(1994, 3, 29)
dateNow = (datetime.datetime.now())

print ("#"*50)
print (f"My age is : {(dateNow - birthDay).days} days.")