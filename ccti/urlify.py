str1 = "Mr. John Smith"


def urlify(string):
    s = ""
    for char in string:
        if char == " ":
            s += '%20'
        else:
            s += char
    return s


print urlify(str1)