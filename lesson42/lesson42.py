# Lesson 42
targetNum = input("Enter a target number: ")
targetNum = int(targetNum)
print("Enter 10 numbers to add to a list, in ascending order: ")
numbersString = input()
numbersList = numbersString.split()
numbersList = [int(i) for i in numbersList]
targetFound = False
for i in range(len(numbersList)):
    for j in range(i + 1, len(numbersList)):
        if numbersList[i] + numbersList[j] == targetNum:
            print("The numbers " + str(numbersList[i]) + " and " + str(numbersList[j]) + " add up to " + str(targetNum))
            targetFound = True
            break
    if targetFound:
        break
if not targetFound:
    print("No two numbers in the list add up to " + str(targetNum))  
# End of Lesson 42  