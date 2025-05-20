sreport = {}
sname = input("Enter the student\'s name : ")
smarks = input("Enter {}\'s marks".format(sname))

sreport[sname] = smarks

srchname = input("Enter the student\'s name : ")

print(sreport.get(srchname, "Student not found"))

