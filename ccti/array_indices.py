import math

arr = [3, 5, 6, 3, 3, 5, 3]


def calculate_combinations_count(n):
    total_pairs = math.factorial(n) / (math.factorial(2) * math.factorial(n-2))
    return total_pairs


def solution(arr):
    d = {}
    count = 0
    for ind, num in enumerate(arr):
        if num in d:
            d[num].append(ind)
        else:
            d[num] = [ind]

    for key in d:
        if len(d[key]) <= 1:
            continue
        elif len(d[key]) == 2:
            count += 1
        else:
            count += calculate_combinations_count(len(d[key]))

    return count


print solution(arr)



