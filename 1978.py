N = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()

# count prime numbers
retval = 0
primes = [2, 3, 5, 7]
notPrimes = [1, 4, 6]
for i in numbers:
    if i > primes[-1] and i > notPrimes[-1]:
        temp = primes[-1] if primes[-1] > notPrimes[-1] else notPrimes[-1]
        while temp <= i:
            temp += 1
            isPrime = True
            for j in primes:
                if temp % j == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(temp)
            else:
                notPrimes.append(temp)
    if i in primes:
        retval += 1
print(retval)
