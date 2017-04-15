from trees_and_graphs.graph import Graph


def visit(node):
    while node:
        print node
        node = node.parent


def dfs(start, count=0):
    if not hasattr(start, 'parent'):
        start.parent = None
    if start.id == 100:
        visit(start)
        count += 1
    for neighbor in start.get_all_neighbors():
        neighbor = g.get_vertex(neighbor)
        neighbor.parent = start
        count = dfs(neighbor, count)
    return count

num_of_steps = 100

g = Graph()

for step in range(1, num_of_steps+1):
    g.add_vertex(step)

all_vertices = g.get_all_vertices()

for vertex in all_vertices:
    vertex_key = vertex.id
    neighbors_id = [vertex_key+1, vertex_key+2]
    for neighbor in neighbors_id:
        if neighbor < len(all_vertices)+1:
            neighbor = g.get_vertex(neighbor)
            vertex.add_neighbor(neighbor)

start = g.get_vertex(1)
print dfs(start)
