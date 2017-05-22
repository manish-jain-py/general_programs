def merge_arr(arr1, arr2):
    c_2 = len(arr2) - 1
    c_m = len(arr1) - 1
    c_1 = (c_m - c_2) - 1
    while c_m > c_1 and c_2 >= 0:
        if c_1 < 0 or arr2[c_2] > arr1[c_1]:
            arr1[c_m] = arr2[c_2]
            c_2 -= 1
        else:
            arr1[c_m] = arr1[c_1]
            c_1 -= 1

        c_m -= 1
    print arr1, arr2


arr1 = [7, 8, 14, 16, 0, 0, 0, 0, 0, 0, 0]
arr2 = [1, 2, 8, 12, 13, 100, 103]
merge_arr(arr1, arr2)