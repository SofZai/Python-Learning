# ---------------------------
# -- Function and return --
# ---------------------------
# [1] A FUNCTION is a reusable block of code do a task
# [2] A FUNCTION run whene you call it
# [3] A FUNCTION accept element to deal called [parameters]
# [4] A FUNCTION can do the task without returning data
# [5] A FUNCTION can return data after job finished
# [6] A FUNCTION create to prevent DRY {Don't Repeat Yous self}
# [7] A FUNCTION accept element whene you call it called [Arguments]
# [8] There's a built-in functions and user defined functions
# [9] A FUNCTION is for all team and apps
# ---------------------------

def function_name () :
    print ("Hello PYTHON from inside FUNCTION")

function_name()

def function_name2 () :
    return "Hello PYTHON from inside FUNCTION"

data = function_name2 ()
print (data)