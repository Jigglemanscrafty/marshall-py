# Lesson 37
def compressString(inputStr):
    compressedStr = ""
    count = 1

    for i in range(1, len(inputStr)):
        if inputStr[i] == inputStr[i - 1]:
            count += 1
        else:
            compressedStr += inputStr[i - 1] + str(count)
            count = 1

    compressedStr += inputStr[-1] + str(count)

    if len(compressedStr) >= len(inputStr):
        return inputStr
    return compressedStr

inputStr = input("Enter a string to compress: ")
compressedStr = compressString(inputStr)
print("Compressed string:", compressedStr)
# End of Lesson 37