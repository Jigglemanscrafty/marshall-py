# Lesson 35
inputList = input("Enter a list of values separated by spaces: ").split()
inputList = [int(num) for num in inputList]

uniqueList = []
for num in inputList:
    if num not in uniqueList:
        uniqueList.append(num)

print("List without dupes:", uniqueList)
# End of Lesson 35