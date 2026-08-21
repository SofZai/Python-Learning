# ------------------------------------
# -- Built in function ==> filter --
# ------------------------------------
# [1] Filter take a function + iterator
# [2] Filter run a function on every element
# [3] The function can be Pre-defined function or Lambda function
# [4] Filter out all elements for which the function return true 
# [5] The function need to return boolean value
# ------------------------------------

# Example 1

def check_num (num) :

    return num > 10

myNum = [1, 5, 17, -4, 23, 0, 0]

filtred_num = filter (check_num, myNum)

for number in filtred_num :
    print (number)

print ("=" * 70)

# Example 2

def check_name (name) :

    return name.startswith ("O") 

myText = ["Sofiane", "Omar", "Kossai"]

filtred_name = filter (check_name, myText)

for per in filtred_name :
    print (per)

print ("=" * 70)

# Example 3

myText = ["Sofiane", "Omar", "Kossai"]

for per in filter (lambda text : text.startswith ("S"), myText) :
    print (per)