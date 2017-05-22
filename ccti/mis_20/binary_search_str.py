str_arr = ["a", "b", "c", "d", "", "", "e", "f", "", "g", "", "j", "", "", "", "z", ""]


def binary_search_str(arr, string):
    start = 0
    end = len(arr) - 1
    while end > start:
        mid = (start + end) / 2
        if arr[mid] == "":
            mid = get_new_mid(mid, arr)
        if arr[mid] == string:
            return mid
        elif string < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


def get_new_mid(mid, arr):
    left_mid = mid - 1
    right_mid = mid + 1
    while left_mid >= 0 or right_mid < len(arr):
        if left_mid >= 0 and arr[left_mid] != "":
            return left_mid
        else:
            left_mid -= 1
        if right_mid <= len(arr) and arr[right_mid] != "":
            return right_mid
        else:
            right_mid += 1

print binary_search_str(str_arr, "z")