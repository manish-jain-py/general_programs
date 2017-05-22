def is_magic_sq(arr):
    pass

arr = [0, 0, 0, 0,
       0, 0, 0, 0,
       0, 0, 0, 0,
       0, 0, 0, 0]

# get all rows
rows = []
ind = 0
n = 2
len_row = n*n

while (ind + len_row) <= len(arr):
    rows.append(arr[ind:ind+len_row])
    ind += len_row

# get all cols
cols = []
blocks = []
i = 0
for row in rows:
    cols.append([])
    blocks.append([])

col_ind = 0
for item in arr:
    cols[col_ind].append(item)
    if col_ind == len_row-1:
        col_ind = 0
    else:
        col_ind += 1

# get all squares
block_ind = 0
for n1 in range(len_row):
    for n2 in range(len_row):
        blocks[block_ind].append(arr[n1][n2])

print blocks
