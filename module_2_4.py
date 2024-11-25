def isPrime(num):
    t = num // 2 + 1
    res = True
    for i in range(2,t):
        if num % i == 0:
            res = False
            break
    return res

numbers = list(map(int,input("Введите числа через пробел: ").split()))

primes = []
not_primes = []

for number in numbers:
    if number != 1:
        if isPrime(number):
            not_primes.append(number)
        else:
            primes.append(number)

print("Primes", primes)
print("Not Primes", not_primes)

