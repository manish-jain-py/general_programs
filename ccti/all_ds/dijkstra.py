from trees_and_graphs.graph import Graph
from priority_queue_extended import PQ
from sys import maxint

graph = Graph()

a = graph.add_vertex('a')
b = graph.add_vertex('b')
c = graph.add_vertex('c')
d = graph.add_vertex('d')
e = graph.add_vertex('e')
f = graph.add_vertex('f')
g = graph.add_vertex('g')
h = graph.add_vertex('h')
i = graph.add_vertex('i')

a.add_neighbor(b, 4)
a.add_neighbor(h, 8)

b.add_neighbor(a, 4)
b.add_neighbor(c, 8)
b.add_neighbor(h, 11)

c.add_neighbor(b, 8)
c.add_neighbor(i, 2)
c.add_neighbor(f, 4)
c.add_neighbor(d, 7)

d.add_neighbor(c, 7)
d.add_neighbor(f, 14)
d.add_neighbor(e, 9)

e.add_neighbor(d, 9)
e.add_neighbor(f, 10)

f.add_neighbor(e, 10)
f.add_neighbor(d, 14)
f.add_neighbor(c, 4)
f.add_neighbor(g, 2)

g.add_neighbor(f, 2)
g.add_neighbor(i, 6)
g.add_neighbor(h, 1)

h.add_neighbor(a, 8)
h.add_neighbor(b, 11)
h.add_neighbor(i, 7)
h.add_neighbor(g, 1)

i.add_neighbor(h, 7)
i.add_neighbor(g, 6)
i.add_neighbor(c, 2)


def apply_dijkstra(graph, source):

    pq = PQ()
    done_dict = {}

    for vertex in graph.get_all_vertices():
        if vertex == source:
            vertex.distance = 0
        else:
            vertex.distance = maxint
        pq.add(vertex.distance, vertex.id)

    while True:
        min_elem_tuple = pq.del_min()
        if min_elem_tuple is None:
            break
        else:
            min_elem = min_elem_tuple[0]
            if min_elem == maxint:
                break
            else:
                curr = min_elem_tuple[1]
                curr = graph.get_vertex(curr)
                for vertex in curr.get_all_neighbors():
                    vertex = graph.get_vertex(vertex)
                    edge_weight = graph.get_edge_weight(curr, vertex)
                    if vertex.id not in done_dict:
                        if curr.distance + edge_weight < vertex.distance:
                            vertex.distance = curr.distance + edge_weight
                            pq.add(vertex.distance, vertex.id)
                done_dict[curr.id] = curr.distance

    return done_dict

print apply_dijkstra(graph, a)





