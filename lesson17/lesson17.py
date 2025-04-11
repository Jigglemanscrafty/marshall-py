# Lesson 17
print("Enter a positive integer:")
num = int(input())

if num < 0:
    print("The number is negative, no factorial.")
elif num == 0:
    print("The factorial is 1.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial is {factorial}.")