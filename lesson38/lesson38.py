# Lesson 38
def isPalindrome(num):
    return str(num) == str(num)[::-1]

largestPalindrome = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if isPalindrome(product) and product > largestPalindrome:
            largestPalindrome = product

print("Largest palindromic number:", largestPalindrome)
# End of Lesson 38