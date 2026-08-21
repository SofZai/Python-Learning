# -----------------------------------
# --File handling ==> read files --
# -----------------------------------

myFile = open (r"C:\Users\CyberTec\Documents\Python\Osama_ELZIRO\Sofiane.txt", "r")

# print (myFile) # File Data object
# print (myFile.name)
# print (myFile.mode)
# print (myFile.encoding) 

# print (myFile.read (5))
# print (myFile.read ())

# print (myFile.readline (5))
# print (myFile.readline ())
# print (myFile.readline ())

# print (myFile.readlines (9))
# print (myFile.readlines ())

for line in myFile :
    print (line)

    if line.startswith ("07") :
        break

myFile.close()