from trees_and_graphs.graph import Graph

def visit(start):
    pass


def run_dfs(start, g):
    print start
    if not hasattr(start, 'parent'):
        start.parent = None
    visit(start)
    for neighbor in start.get_all_neighbors():
        print vertex.id
        neighbor = g.get_vertex(neighbor)
        neighbor.parent = vertex
        run_dfs(neighbor, g)


g = Graph()

string = "abcd"
len_str = len(string)

for char in string:
    g.add_vertex(char)

for i in range(len_str):
    vertex = g.get_vertex(string[i])
    for j in range(i+1, len_str):
        neighbor = g.get_vertex(string[j])
        g.add_edge(vertex, neighbor)

print g

for vertex in g.get_all_vertices()[:1]:
    run_dfs(vertex, g)
