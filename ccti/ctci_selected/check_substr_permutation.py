"""
find how many substrings of str1 can be permutations of str2
"""


def find_permutations_count(len_sub_str, len_str1, str2, str1):

    ind = 0
    prev_ind = -1
    count = 0
    dict_str2 = make_dict(str2)
    sub_str = str1[ind:len_sub_str]
    dict_str1 = make_dict(sub_str)

    while prev_ind < (len_str - len_sub_str):
        dict_str1 = get_new_substr_dict(dict_str1, str1, prev_ind, len_sub_str)
        if is_perm(dict_str1, dict_str2):
            count += 1
        prev_ind += 1

    return count


def get_new_substr_dict(dict_str1, str1, prev_ind, len_sub_str):

    if prev_ind == -1:
        return dict_str1

    if dict_str1[str1[prev_ind]] > 1:
        dict_str1[str1[prev_ind]] -= 1
    else:
        dict_str1.pop(str1[prev_ind])

    if str1[prev_ind+len_sub_str] in dict_str1:
        dict_str1[str1[prev_ind+len_sub_str]] += 1
    else:
        dict_str1[str1[prev_ind + len_sub_str]] = 1

    return dict_str1


def is_perm(d1, d2):
    for key in d1.keys():
        val1 = d1[key]
        val2 = d2.get(key, 0)
        if val1 == val2:
            pass
        else:
            return False
    return True


def make_dict(string):
    d = {}
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d


print find_permutations_count(4, 11, "cAda", "AbrAcAdAbrA")