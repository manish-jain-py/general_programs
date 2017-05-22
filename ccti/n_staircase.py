def find_ways(n):
    if n <= 2:
        return n
    else:
        return (n-2) + (n-1)


print find_ways(3)