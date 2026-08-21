# ------------------------------------
# -- Built in function ==> Reduce --
# ------------------------------------
# [1] Reduce take a function + iterator
# [2] Reduce run a function on first and second element and give result
# [3] Then run function on result and third element
# [4] Then run function on result and fourth element and so on
# [5] Till one element is left and this is the result of the reduce
# [6] The function can be pre-defined function or lambda function
# ------------------------------------

from functools import reduce

def sumAll (num1, num2) :
    return num1 + num2

numbers = [1, 4, 55, 80, 100]

result = reduce (sumAll, numbers)
print (result)



print (reduce (lambda n1, n2 : n1 + n2, numbers))