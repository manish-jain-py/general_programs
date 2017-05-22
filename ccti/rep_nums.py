num_arrs = [[100, 200], [52, 80], [57, 64], [74, 78]]

for nums in num_arrs:
    start = nums[0]
    end = nums[1]
    s = set()
    count = 0
    for i in range(start, end+1):
        if len(set(str(i))) != len(str(i)):
            count += 1
    print count