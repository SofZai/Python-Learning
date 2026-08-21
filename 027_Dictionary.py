# ------------------
# -- Dicyionary --
# ------------------

# [1] Dict Items Are Enclosed In Curly Braces {}
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need to be Immutable ==> (Numbers, Strings, Tuples) Lists Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Uniaue
# [6] Dict Is Not Ordered, You Access Its Elements With Key
# -------------------------------------------

user = {
    "name" : "Sofiane",
    "age" : 32,
    "country" : "Algeria",
    "skils" : ["html", "matlab", "py"],
    "rating" : 10.5,
}

print (user)
print (user["country"])
print (user.get("country"))
print (user.keys())
print (user.values())

print ("=" * 40)

# Two-Dimentional Dictionary

languages = {
    "one" : {
        "name" : "Html",
        "progress" : "80%"
    },
    "Two" : {
        "name" : "Css",
        "progress" : "90%"
    },
    "Three" : {
        "name" : "Js",
        "progress" : "70%"
    }
}
print (languages)
print (languages["one"])
print (languages["Three"]["progress"])
print (len(languages))
print (len(languages["Two"]))

# Creat e Dictionary From Variables

frameWorkOne = {
    "name" : "Sofiane",
    "age" : 31
}

frameZorkTwo = {
    "name" : "Kossai",
    "age" : 3.5
}

frameWorkThree = {
    "name" : "Mossab",
    "age" : 0.2
}

allFrameWork = {
    "one" : frameWorkOne,
    "two" : frameZorkTwo,
    "three" : frameWorkThree
}

print (allFrameWork)