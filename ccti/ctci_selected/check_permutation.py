def is_permutation(str1, str2):

    d_str1, d_str2 = {}, {}

    for char in str1:
        if char in d_str1:
            d_str1[char] += 1
        else:
            d_str1[char] = 1
    for char in str2:
        if char in d_str2:
            d_str2[char] += 1
        else:
            d_str2[char] = 1

    for key in d_str1.keys():
        val1 = d_str1[key]
        val2 = d_str2.get(key)
        if val1 == val2:
            d_str1.pop(key)
            d_str2.pop(key)
        else:
            return False

    if len(d_str1) !=0 or len(d_str2) != 0:
        return False

    return True

print is_permutation("amanishk", "shimana")


