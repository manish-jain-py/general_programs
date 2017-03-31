from graph import Graph


def DFS(current_vertex, g, all_paths=[]):
    if not hasattr(current_vertex, 'parent'):
        current_vertex.parent = None
    if len(current_vertex.get_all_neighbors()) == 0:
        ones, path = traverse(current_vertex)
        all_paths.append((ones, path))
    for neighbor in current_vertex.get_all_neighbors():
        neighbor_vertex = g.get_vertex(neighbor)
        neighbor_vertex.parent = current_vertex

        DFS(neighbor_vertex, g)
    return all_paths


def traverse(node):
    ones = 0
    path = []
    while node:
        path.append(node.id)
        ones += node.value
        node = node.parent
    path.reverse()
    return ones, path


n = [[0, 1, -1, 0], [1, 0, 1, -1], [1, 1, 0, 1], [0, 1, 0, 0]]

g = Graph()
row = len(n); col = len(n)
for i in range(row):
    for j in range(col):
        if n[i][j] != -1:
            vertex = g.add_vertex((i,j))
            vertex.value = n[i][j]

for v in g.get_all_vertices():
    main_vertex = v
    i,j = v.id
    if i+1 < row:
        child = g.get_vertex((i+1,j))
        if child:
            main_vertex.add_neighbor(child)
    if j+1 < col:
        child = g.get_vertex((i, j+1))
        if child:
            main_vertex.add_neighbor(child)

for v in g.get_all_vertices():
    v.visited = False

start = g.get_vertex((0,0))

all_paths = DFS(start,g)

print len(all_paths)
