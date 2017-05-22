def visit(node):
    while node:
        print node.id,
        node = node.parent
    print


def run_dfs(start, perm='', perm_set=set()):
    if start.id in perm:
        perm_set.add(perm)
        return perm_set
    else:
        perm += start.id
    for neighbor in start.get_all_neighbors():
        neighbor = g.get_vertex(neighbor)
        if neighbor != start:
            neighbor.parent = start
            run_dfs(neighbor, perm, perm_set)
    return perm_set

from trees_and_graphs.graph import Graph

g = Graph()

string = "abc"

for char in string:
    g.add_vertex(char)

for i, char in enumerate(string):
    v = g.get_vertex(char)
    for j in range(i+1, len(string)):
        neighbor = g.get_vertex(string[j])
        g.add_edge(v, neighbor)
        g.add_edge(neighbor, v)

for v in g.get_all_vertices():
    v.parent = None
    set_final = run_dfs(v)

print set_final
print len(set_final)

#print g