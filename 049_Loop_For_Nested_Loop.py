# ---------------------
# -- Loop ===> for --
# --- Nested Loop ---
# ---------------------

# peoples = ["Sofiane", "Kossai", "Asma", "Mossab"]
# skils = ["Html", "Css", "Js"]

# for name in peoples :             # Outer Loop
#     print (f"{name} skills are: ")
#     for skil in skils :           # Inner Loop
#         print (f"- {skil}")

peoples = {
    "Sofiane" : {
        "Html" : "70%",
        "Css" : "80%",
        "Js" : "70%"
    },
     "Kossai" : {
        "Html" : "90%",
        "Css" : "80%",
        "Js" : "90%"
    },
     "Mossab" : {
        "Html" : "70%",
        "Css" : "60%",
        "Js" : "90%"
    }
}


# print (peoples ["Sofiane"] )
# print (peoples ["Sofiane"] ["Css"])

for name in peoples :
    print (f"skils and progres for {name} are :")
    for skil in peoples[name] :
        print (f"{skil} ==> {peoples [name] [skil]}")