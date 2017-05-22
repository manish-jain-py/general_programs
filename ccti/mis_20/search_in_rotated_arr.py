def find_rotation_point(arr):

    len_arr = len(arr)
    mid = len_arr/2
    start = 0
    end = len_arr - 1
    while end > start:
        if is_rotation_point(mid, arr):
            return mid
        elif arr[mid] < arr[start]:
            end = mid - 1
            mid = end/2
        elif arr[mid] > arr[end]:
            start = mid + 1
            mid = (start + end) / 2
    return None


def is_rotation_point(mid, arr):

    if arr[mid - 1] < arr[mid] < arr[mid + 1]:
        return False
    else:
        return True


def find_element_b_s(elem, arr, start=0, end=-1):

    if end == -1:
        end = len(arr) - 1
    while end > start:
        print start, end
        mid = (start + end) / 2
        if arr[mid] == elem:
            return mid
        elif elem < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


arr = [16, 17, 3, 5, 6, 7, 8, 9, 10, 12, 14]
element = 10
point = find_rotation_point(arr)

#print find_element_b_s(15, arr)

