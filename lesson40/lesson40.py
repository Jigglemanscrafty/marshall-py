# Lesson 40
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def listPrimes(n):
    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    return primes

n = int(input("Enter a positive integer: "))
primes = listPrimes(n)
print("Prime numbers under", n, ":", primes)
# End of Lesson 40