def fib(n, l=[0,1]):
    if n == 0:
        return l[0]
    if n == 1:
        return l[1]
    if n > len(l):
        l.append(fib(n-1) + fib(n-2))
        print "non-repititive"
        return l[-1]
    else:
        return l[n-1]

print fib(10)