from trees_and_graphs.graph import Graph


def has_cycle(graph, source, parent=None, cycle=False):
    set_white.remove(source.id)
    set_grey.add(source.id)
    for neighbor in source.get_all_neighbors():
        neighbor = graph.get_vertex(neighbor)
        if neighbor.id in set_black or neighbor == parent:
            continue
        if neighbor.id in set_grey:
            return True
        else:
            cycle = has_cycle(graph, neighbor, source)
            if cycle:
                break
    set_grey.remove(source.id)
    set_black.add(source.id)
    return cycle

graph = Graph()

a = graph.add_vertex('a')
b = graph.add_vertex('b')
c = graph.add_vertex('c')
d = graph.add_vertex('d')
e = graph.add_vertex('e')
f = graph.add_vertex('f')

a.add_neighbor(b)
a.add_neighbor(f)

b.add_neighbor(a)
b.add_neighbor(e)
b.add_neighbor(c)

c.add_neighbor(b)
c.add_neighbor(d)

d.add_neighbor(e)
d.add_neighbor(c)

e.add_neighbor(b)
e.add_neighbor(d)

f.add_neighbor(a)

set_white = set()
set_grey = set()
set_black = set()

for vertex in graph.get_all_vertices():
    set_white.add(vertex.id)

print has_cycle(graph, a)