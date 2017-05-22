from math import sqrt

max_num = 51

num_list = [True for i in range(max_num+1)]

num_list[0], num_list[1] = False, False

for prime in range(2, int(sqrt(max_num))):

    for num in range(prime * prime, max_num + 1):

        if num_list[num] is True:

            if num % prime == 0:

                num_list[num] = False

print [ind for ind, item in enumerate(num_list) if item is True]
