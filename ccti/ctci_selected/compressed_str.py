def compress_string(string):
    repeat_count = 0
    prev_char = ''
    new_str = ''
    for ind, char in enumerate(string):
        if prev_char == char or prev_char == '':
            repeat_count += 1
            if ind == len(string)-1:
                new_str += prev_char + str(repeat_count)
        else:
            new_str += prev_char + str(repeat_count)
            repeat_count = 1
        prev_char = char

    if len(string) > len(new_str):
        return new_str
    else:
        return string

print compress_string("aabccccaaaaa")