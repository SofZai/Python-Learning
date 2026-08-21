# ------------------------------------------------------
# -- Function packing, unpacking arguments training --
# ------------------------------------------------------

mySkillsTuple = ("Html", "CSS", "JS")
mySkillsDict = {
    "Python" : "90%",
    "SQL" : "80%"
}

def show_skills (name, *skills, **skillsWithProgress) :
    print (f"Hello {name} \nyour skills without progress are: ")
    for skill in skills :
        print (f"- {skill}")
    
    print ("your skills with progress are: ")
    for skill_key, skill_value in skillsWithProgress.items() :
        print (f"- {skill_key} ==> {skill_value}")

show_skills ("Sofiane", *mySkillsTuple, **mySkillsDict )