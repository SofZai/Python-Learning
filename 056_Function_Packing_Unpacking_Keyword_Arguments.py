# ------------------------------------------------------
# -- Function packing, unpacking arguments **KWargs --
# ------------------------------------------------------

# def show_skills (*skills) :
#     print (type (skills))
#     for skill in skills :
#         print (skill)

# show_skills ("Html", "CSS")

def show_skills (**skills) :
    print (type (skills))
    for skill, value in skills.items () :
        print (f"{skill} ==> {value}")

show_skills (Html = "60%", Css = "90%")