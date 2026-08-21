# ---------------------------------
# -- Built in function ==> Map --
# ---------------------------------
# [1] Map take a function + iterator
# [2] Map called map because it map the function on every element
# [3] The function can be Pre-defined function or Lambda function
# ---------------------------------

# Use map with pre-defined function

def formatText (text) :
    return f"- {text.strip().capitalize()} -"

myText = ["Sofiane", "KOssai", "mosSAb"]

formatedText = map (formatText, myText)
# print (formatedText)

for name in formatedText :
    print (name)

###########################################

# Use map with lambda function

myText = ["Sofiane", "KOssai", "mosSAb"]

for name in map (lambda text : f"- {text.strip().capitalize()} -", myText) :
    print (name)