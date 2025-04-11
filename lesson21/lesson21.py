# Lesson 21
n = int(input("Enter a positive integer greater than 1: "))

maxFactors = 0
numberWithMaxFactors = 0

for num in range(1, n + 1):
    factorsCount = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factorsCount += 1
    if factorsCount > maxFactors:
        maxFactors = factorsCount
        numberWithMaxFactors = num

print(f"The number with the most factors from 1 to {n} is {numberWithMaxFactors}")
# End of Lesson 21