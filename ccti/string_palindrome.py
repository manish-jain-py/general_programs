def magic(string):
    len_str = len(string)
    str_counter = 0
    str_array = []
    for i in range(len_str, 1, -1):
        str_array.append(string[str_counter]*i)
        str_counter += 1

magic('abc')


