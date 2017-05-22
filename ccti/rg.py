def solution(A, B):

    a_str = str(A)
    b_str = str(B)

    new_num = []

    counter_a = 0
    counter_b = 0
    for i in range(len(a_str) + len(b_str)):

        if counter_a < len(a_str):
            new_num.append(a_str[counter_a])
            counter_a += 1

        if counter_b < len(b_str):
            new_num.append(b_str[counter_b])
            counter_b += 1

    return ''.join(new_num)


from collections import deque


def add_children(start, m, n):

    children = []
    right_x = start[0] + 1
    right_y = start[1]
    if right_x < m and right_y < n:
        children.append((right_x, right_y))
    down_x = start[0]
    down_y = start[1] + 1
    if down_x < m and down_y < n:
        children.append((down_x, down_y))

    if not children:
        print start

    return children


def bfs(matrix):

    d = deque()
    m = len(matrix)
    n = len(matrix[0])
    print m, n
    final_set = set()

    start = (0, 0)
    d.append(start)
    final_set.add(start)

    while d:
        parent = d.popleft()
        children = add_children(parent, m, n)

        for child in children:
            if matrix[parent[0]][parent[1]] == matrix[child[0]][child[1]]:
                pass
                # print parent, children
                # print matrix[parent[0]][parent[1]], matrix[child[0]][child[1]]
            else:
                final_set.add(child)
            d.append(child)

        final_set_copy = set()
        for item in final_set:
            final_set_copy.add(item)

        for item in final_set:
            x = item[0]
            y = item[1]
            for item2 in final_set:
                x2 = item2[0]
                y2 = item[1]
                if item != item2 and (((x+1) == x2 and y == y2) or ((y+1) == y2 and x == x2)):
                    if item2 in final_set_copy:
                        final_set_copy.remove(item2)

    return final_set_copy

matrix = [
    [5, 4, 4],
    [4, 3, 4],
    [3, 2, 4],
    [2, 2, 2],
    [3, 3, 4],
    [1, 4, 4],
    [4, 1, 1]
]

print bfs(matrix)



