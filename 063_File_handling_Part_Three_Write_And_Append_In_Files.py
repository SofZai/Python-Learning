# ---------------------------------------------------
# -- File handling ==> write and append in files --
# ---------------------------------------------------

# myFile = open (r"C:\Users\CyberTec\Documents\Python\Osama_ELZIRO\Sofiane.txt", "w")
# myFile.write ("Hello Python\n")
# myFile.write ("Hello from Python\n")

# myFile = open (r"C:\Users\CyberTec\Documents\Python\Osama_ELZIRO\Fun.txt", "w")
# myFile.write ("Hello Python\n" * 1000)

# myList = ["Sofiane\n", "Asma\n", "Kossai\n", "Mossab\n"]
# myFile = open (r"C:\Users\CyberTec\Documents\Python\Osama_ELZIRO\Files\Sofiane.txt", "w")
# myFile.writelines (myList)

myFile = open (r"C:\Users\CyberTec\Documents\Python\Osama_ELZIRO\Files\Sofiane.txt", "a")
myFile.write ("Hello Python\n")
myFile.write ("Hello from Python\n")
