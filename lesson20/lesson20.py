# Lesson 20
perfect = 0

for number in range(1, 10000):
    divisorsSum = 0
    for i in range(1, number):
        if number % i == 0:
            divisorsSum += i
    if divisorsSum == number:
        perfect += number

print(f"Sum of perfect numbers under 10,000: {perfect}")
# End of Lesson 20