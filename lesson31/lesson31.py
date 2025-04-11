# Lesson 31
stringA = input("Enter first string: ")
stringB = input("Enter second string: ")

stringA = stringA.lower()
stringB = stringB.lower()

listA = list(stringA)
listB = list(stringB)

listA.sort()
listB.sort()

if listA == listB:
    print("Anagrams")
else:
    print("Not Anagrams")
# End of lesson 31