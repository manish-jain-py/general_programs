matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

new_matrix = []


def rotate_matrix():
    for i in range(len(matrix[0])):
        new_matrix.append([])
    new_row = 0
    len_row = len(matrix[0])
    for row in reversed(matrix):
        for item in row:
            new_matrix[new_row].append(item)
            new_row += 1
            if new_row == len_row:
                new_row = 0


for row in matrix:
    print row
rotate_matrix()
print '......'
for row in new_matrix:
    print row