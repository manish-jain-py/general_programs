matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


def rotate_matrix():
    row_start = 0
    row_end = len(matrix) - 1
    col_start = 0
    col_end = len(matrix[0]) - 1
    while row_end > row_start:
        side1_col = range(row_start, row_end)
        row1 = row_start
        side2_row = range(col_start, col_end)
        col2 = col_end
        side3_col = range(row_end, row_start, -1)
        row3 = row_end
        side4_row = range(col_end, col_start, -1)
        col4 = col_start
        for col1, row2, col3, row4 in zip(side1_col, side2_row, side3_col, side4_row):

            # move side 1 to side 2
            temp = matrix[row2][col2]
            matrix[row2][col2] = matrix[row1][col1]

            # move side 2 to side 3
            temp2 = matrix[row3][col3]
            matrix[row3][col3] = temp

            # move side 3 to side 4
            temp3 = matrix[row4][col4]
            matrix[row4][col4] = temp2

            # move side 4 to side 1
            matrix[row1][col1] = temp3

        row_start += 1
        col_start += 1
        row_end -= 1
        col_end -= 1


for row in matrix:
    print row
rotate_matrix()
print "......"
for row in matrix:
    print row

