from math import sqrt

n = 600851475143
a = [2, 3, 4, 5, 6, 7, 8, 9]
primes = []

for i in range(int(sqrt(n)) + 1):
    check = []
    if n % i == 0:
        for item in a:
            if i % item == 0:
                check.append(1)
            else:
                check.append(0)
        if sum(check) == 0:
            primes.append(i)
    print(max(primes))
    
