# -------------------------
# -- Built In Function --
# -------------------------
# enumerate ()
# help ()
# reversed ()
# -------------------------

# enumerate (iterable, start = 0)

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate (mySkills, 1)

for counter, skill in mySkillsWithCounter :
    print (f"{counter} : {skill}")

print ("#" * 50)

# help ()

print (help (print))

print ("#" * 50)

# reversed (iterable)

myString = "KosMos"

print (reversed (myString))

for s in reversed (myString) :
    print ((s))

for k in reversed (mySkills) :
    print (k)