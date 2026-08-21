# -------------------------------
# -- Loop ==> While training --
# -- Simple Bookmarks Manage --
# -------------------------------

myWebs = []
maxWebs = 5

while maxWebs > 0 :
    web = input ("Website name without https:// ")

    myWebs.append(f"https://{web.strip().lower()}")
    maxWebs -= 1
    print (f"Website added, {maxWebs} place left")

print (myWebs)

if len (myWebs) > 0:
    myWebs.sort()

index = 0
while index < len (myWebs) :
    print (myWebs [index])
    index += 1
    