

def make_zero(matrix):
    zero_elem_list = []
    element_positions = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 0:
                element_positions.append((row, col))
    # get rows elements to be made 0
    for pos in element_positions:
        row = pos[0]
        zero_elem_list += [(row, i) for i in range(num_cols)]
        col = pos[1]
        zero_elem_list += [(i, col) for i in range(num_rows)]
    for pos in zero_elem_list:
        matrix[pos[0]][pos[1]] = 0
    print matrix


matrix = [[1, 4, 6, 7],
          [2, 1, 9, 3],
          [0, 3, 8, 0]]
make_zero(matrix)