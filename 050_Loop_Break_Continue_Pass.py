# ---------------------------
# -- Break Continue Pass --
# ---------------------------

myNembers = [1, 2, 3, 4, 5, 7, 12, 33]

# Continue

for number in myNembers :
     if number == 4 :
          continue 
     
     print (number)


print ("=" * 40)

# Break

for number in myNembers :
     
     if number == 4 :
          break
     
     print (number)

print ("=" * 40)

# Pass

for number in myNembers :
     
     if number == 4 :
         
         pass
     
     print (number)
     
