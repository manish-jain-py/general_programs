def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        count = 2
        while count <= n:
            count += 1
            sum = a + b
            a = b
            b = sum
    return sum

print fib(10)
