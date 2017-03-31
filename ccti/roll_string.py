s = 'abc'
operations = [[0,0,'L'],[2,2,'L'],[0,2,'R']]

def rolling_string(s, operations):
    for op in operations:
        beg = op[0]
        end = op[1]
        operation = op[2]
        if operation == 'L':
            for char in s[beg:end+1]:
                if char == 'a':
                    new_char = 'z'
                else:
                    new_char = chr(ord(char)-1)
                s = s[:beg] + new_char + s[beg+1:]
                beg += 1
        else:
            for char in s[beg:end+1]:
                if char == 'z':
                    new_char = 'a'
                else:
                    new_char = chr(ord(char)+1)
                s = s[:beg] + new_char + s[beg + 1:]
                beg += 1


    return s


print rolling_string(s, operations)