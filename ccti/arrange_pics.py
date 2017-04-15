string = """photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11"""


def fetch_date_time(photo):
    return photo.split(', ')[2]


def prefixed_number(n, max_n):
    len_n = len(str(n))
    len_max_n = len(str(max_n))
    prefix = ''.join(['0' for i in range(len_max_n-len_n)]) + str(n)
    return prefix


def solution(S):

    list_of_pics = S.split('\n')

    city_dict = {}

    for pic in list_of_pics:
        city = pic.split(', ')[1]
        if city in city_dict:
            city_dict[city].append(pic)
        else:
            city_dict[city] = [pic]

    final_string = ""

    for city_group in city_dict:
        city_dict[city_group].sort(key=fetch_date_time)
        for ind, photo in enumerate(city_dict[city_group]):
            city = photo.split(',')[1]
            ext = photo.split(', ')[0].split('.')[-1]
            max_len = len(city_dict[city_group])
            number = prefixed_number(ind+1, max_len)
            city_dict[city_group][ind] = city + number + '.' + ext + '\n'
        final_string += ''.join(city_dict[city_group])

    return final_string

print solution(string)