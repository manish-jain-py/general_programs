

def is_palindrome(str1):
    str_dict = str_to_dict(str1)
    count_ones = 0
    for key in str_dict:
        if str_dict[key] % 2 == 1:
            count_ones += 1
    if count_ones > 1:
        return False
    else:
        return True


def str_to_dict(str1):
    d = {}
    for char in str1:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

str1 = "aba abac"

print is_palindrome(str1)

