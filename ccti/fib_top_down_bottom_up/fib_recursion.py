def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    sum = fib(n-1) + fib(n-2)
    print sum
    return sum

print fib(10)