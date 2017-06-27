fib_sum = 0


def fib_list(N):
    fibs = [1, 2]
    while max(fibs) < N:
        fibs.append(sum(fibs[-2:]))
    return fibs


for item in fib_list(4E6):
    if item % 2 == 0:
        fib_sum += item

print(fib_sum)
