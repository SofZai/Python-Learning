# --------------------
# -- Loop ==> For --
# --------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numbers :
    print (f"{str (n).zfill(2).center(20, "-")}")

    if n % 2 == 0 :
        print (f"the number {str (n).zfill(2)} is Even")
    else :
        print (f"the number {str (n).zfill(2)} is odd")
else :
    print ("Loop is finished")

myName = "Sofiane"

for l in myName :
    print (l.upper())