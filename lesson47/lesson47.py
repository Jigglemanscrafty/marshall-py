# Lesson 47
def sumNumbers(n):
    if n == 1:
        return 1
    else:
        return n + sumNumbers(n - 1)

n = int(input("Enter a positive integer greater than 1: "))
result = sumNumbers(n)
print("Sum of numbers from", n, "to 1 is:", result)
# End of Lessons