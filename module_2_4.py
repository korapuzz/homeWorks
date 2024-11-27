def isPrime(num):
    t = num // 2 + 1
    return all([num % i for i in range(2, t)])

numbers = list(map(int,input("Введите числа через пробел: ").split()))

primes = []
not_primes = []

for number in numbers:
    if number != 1:
        if isPrime(number):
            primes.append(number)
        else:
            not_primes.append(number)

print("Primes", primes)
print("Not Primes", not_primes)
