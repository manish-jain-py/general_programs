from graph import Graph
from graph import Vertex

def create_graph():
    g = Graph()
    for node in ['a','b','c','d','e','f','g']:
        g.add_vertex(node)

    a = g.get_vertex('a')
    b = g.get_vertex('b')
    c = g.get_vertex('c')
    d = g.get_vertex('d')
    e = g.get_vertex('e')
    f = g.get_vertex('f')
    gv = g.get_vertex('g')

    # add edges (ccti page 250)

    a.add_neighbor(e)
    f.add_neighbor(c)
    f.add_neighbor(b)
    f.add_neighbor(a)
    c.add_neighbor(a)
    b.add_neighbor(a)
    b.add_neighbor(e)
    d.add_neighbor(gv)
    d.add_neighbor(b)
    e.add_neighbor(f)

    return g

if __name__ == '__main__':
    print create_graph()