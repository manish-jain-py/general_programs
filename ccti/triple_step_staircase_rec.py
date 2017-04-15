def ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return ways(n-1) + ways(n-2) + ways(n-3)

print ways(3)