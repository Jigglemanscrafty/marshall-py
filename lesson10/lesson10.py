# Lesson 10
print("Enter the first digit:")
firstDigit = input().strip()

print("Enter the second digit:")
secondDigit = input().strip()

print("Enter the third digit:")
thirdDigit = input().strip()

print("Enter the fourth digit:")
fourthDigit = input().strip()

if firstDigit in {"8", "9"}:
    if secondDigit == thirdDigit:
        if fourthDigit in {"8", "9"}:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")
# End of Lesson 10