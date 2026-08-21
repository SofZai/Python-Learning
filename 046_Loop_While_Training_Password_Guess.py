# -------------------------------
# -- Loop ==> While Training --
# --- Simple Password Guess --- 
# -----------------------------

tries = 4

mainPassword = "aSo=29"
inputPassword = input ("Enter your password ")

while inputPassword != mainPassword :
    print ("Wrong password")
    tries -= 1

    if tries == 0 :
        print ("Tries Expired")
        break
    else :
         print (f"{"Last" if tries == 1 else tries} tries left !")
         inputPassword = input ("Enter your password ")
    
else :
    print ("Correct Password")
