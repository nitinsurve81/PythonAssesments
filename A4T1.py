try:
    file1 = open("A4T1.txt","r")
    rf = file1.read()
    print(rf)
    file1.close()
except:
    print("File does not exist")