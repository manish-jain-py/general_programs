s = "1(2)2(3)26#(2)24#"
s = '23#(2)24#25#26#23#(3)'
def frequency(s):
    d = {}
    for ind, i in enumerate(s[:]):
        if i == '#':
            code = s[ind - 2] + s[ind - 1]
            if (ind + 1) < len(s) and s[ind + 1] == '(':
                freq = s[ind + 2:].split(')')[0]
                if d.get(code):
                    d[code] += int(freq)
                else:
                    d[code] = int(freq)
                sub_str = code + '#(' + freq + ')'
                new_sub = ''.join(['@' for x in sub_str])
                s = s[:ind - 2] + s[ind - 2:].replace(sub_str, new_sub)
            else:
                freq = 1
                if d.get(code):
                    d[code] += int(freq)
                else:
                    d[code] = int(freq)
                sub_str = code + '#'
                new_sub = ''.join(['@' for x in sub_str])
                s = s[:ind - 2] + s[ind - 2:].replace(sub_str, new_sub)

    print s
    for ind, i in enumerate(s[:]):
        if i == '@':
            continue
        else:
            code = s[ind]
            if (ind + 1) < len(s) and s[ind + 1] == '(':
                freq = s[ind + 2:].split(')')[0]
                if d.get(code):
                    d[code] += freq
                else:
                    d[code] = freq
                sub_str = code + '(' + freq + ')'
                new_sub = ''.join(['@' for x in sub_str])
                s = s[:ind] + s[ind:].replace(sub_str, new_sub)
            else:
                freq = 1
                if d.get(code):
                    d[code] += freq
                else:
                    d[code] = freq
                sub_str = code
                new_sub = ''.join(['@' for x in sub_str])
                s = s[:ind] + s[ind:].replace(sub_str, new_sub)

    final_list = []
    for num in range(1,27):
        if d.get(str(num)):
            final_list.append(d[str(num)])
        else:
            final_list.append(0)

    print d
    print s
    return final_list

print frequency(s)