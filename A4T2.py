fdata = input("Enter something to enter in the file ")
try:
    file = open("A4T2.txt","w")
    wrtf2 = file.write(fdata+"\n")
    print("Data successfully written to A4T2.txt")

    file.close()

    mdata = input("Enter additional text to append ")

    file = open("A4T2.txt","a")
    wrtfile = file.write(mdata)
    print("Data successfully appended")
    file.close()

    file = open("A4T2.txt","r")
    rf3 = file.read()
    print(rf3)
    file.close()

except:
    print("file does not exist ")
