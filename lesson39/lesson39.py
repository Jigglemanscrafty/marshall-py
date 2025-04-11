# Lesson 39
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print("Greatest Common Divisor:", result)
# End of Lesson 39