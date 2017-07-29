import timeit


def is_palindrome(val):
    a = str(val)
    return a == a[::-1]


num = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        a = i * j
        if a > num and is_palindrome(a):
            num, x, y = a, i, j

print("%3d x %3d = %6d" % (x, y, num))
