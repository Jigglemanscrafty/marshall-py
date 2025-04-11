# Lesson 19
factors = set()
num = int((input("Enter a number: ")))
for i in range(1, num + 1):
    if num % i == 0:
        factors.add(i)
if factors == {1, num}:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
# End of Lesson 19