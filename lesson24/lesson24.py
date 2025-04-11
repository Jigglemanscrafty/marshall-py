# Lesson 24
nameList = []

keepGoing = True
while keepGoing:
    name = input("Enter a name, or X to end program: ")
    if name == "X":
        keepGoing = False
    else:
        nameList.append(name)

sortedList = sorted(nameList, key=len)
print(sortedList[-1]) 
# End of Lesson 24