string = "nbaacbnad"

list_of_chars = []
list_of_counts = []

for char in string:
    if char in list_of_chars:
        ind = list_of_chars.index(char)
        list_of_counts[ind][1] += 1
    else:
        list_of_chars.append(char)
        list_of_counts.append([len(list_of_counts), 1])

print list_of_chars, list_of_counts


def get_second_elem(l):
    return l[-1]


def get_first_elem(l):
    return l[0]


list_of_counts.sort(key=get_second_elem, reverse=True)
new_list = sorted(list_of_counts[:3], key=get_first_elem)

for elem in new_list:
    print list_of_chars[elem[0]]