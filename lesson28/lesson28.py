# Lesson 28
print("Enter string:")
userInput = input()
userInput = userInput.upper()
userInput = list(userInput)

for i in sorted(userInput):
    sortUserInput = userInput.copy()
for i in sorted(userInput, reverse=True):
    reversedUserInput = userInput.copy()

if sortUserInput == reversedUserInput:
    print("Palindrome")
else:
    print("Not a palindrome")
# End of lesson 28