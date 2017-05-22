from trees_and_graphs.graph import Graph

power_set = []

def visit(n):
    obj_set = []
    while n:
        obj_set.append(n.id)
        n = n.parent
    power_set.append(obj_set)


def dfs(vertex, g):
    visit(vertex)
    for neighbor in vertex.get_all_neighbors():
        neighbor = g.get_vertex(neighbor)
        neighbor.parent = vertex
        dfs(neighbor, g)


obj_list = ['a', 'b', 'c']
len_list = len(obj_list)

g = Graph()

for obj in obj_list:
    g.add_vertex(obj)

for i in range(len_list-1):
    for j in range(i+1, len_list):
        from_v = g.get_vertex(obj_list[i])
        to_v = g.get_vertex(obj_list[j])
        g.add_edge(from_v, to_v)

for vertex in g.get_all_vertices():
    vertex.parent = None
    dfs(vertex, g)

print power_set
