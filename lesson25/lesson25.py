# Lesson 25
num = int(input("Enter a number greater than 1: "))
factor = 2
largest_prime = 0

while factor * factor <= num:
    if num % factor == 0:
        largest_prime = factor
        num //= factor
    else:
        factor += 1

if num > 1:
    largest_prime = num

print("The largest prime factor is", largest_prime)
# End of Lesson 25