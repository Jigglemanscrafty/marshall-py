# Lesson 18
factors = set()
num = int((input("Enter a number: ")))
for i in range(1, num + 1):
    if num % i == 0:
        factors.add(i)
print(f"The factors of {num} are: {factors}")
# End of Lesson 18