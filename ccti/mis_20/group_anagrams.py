def group_anagrams_naive(arr):
    for i in range(0, len(arr)):
        next_anagram = i + 1
        for j in range(i+1, len(arr)):
            if is_anagram(arr[i], arr[j]) and j != next_anagram:
                swap(j, next_anagram, arr)
                next_anagram += 1
    return arr


def group_anagrams_better(arr):
    i = 0
    while i < len(arr):
        next_anagram = i + 1
        for j in range(i+1, len(arr)):
            if is_anagram(arr[i], arr[j]) and j != next_anagram:
                swap(j, next_anagram, arr)
                next_anagram += 1
                i += 1
        i += 1
    return arr


def group_anagram_eff(arr):
    return sorted(arr, key=sort_string)


def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    d = {}

    for char in str1:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for char in str2:
        if char in d:
            d[char] -= 1
            if d[char] == 0:
                del(d[char])
        else:
            return False

    if d.keys():
        return False
    return True


def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def sort_string(string):
    return ''.join(sorted(string))


str_arr = ["man", "mani", "nmij", "nam", "jmni", "inam", "amn", "mnij", "jimn"]
print group_anagram_eff(str_arr)