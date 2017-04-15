from sample_graph import create_graph


def has_cycle(curr, g, cycle=False):
    if curr.color == 'white':
        curr.color = 'grey'
        for child in curr.get_all_neighbors():
            child = g.get_vertex(child)
            child.parent = curr
            if child.color == 'grey':
                traverse(child)
                return True
            else:
                cycle = has_cycle(child, g)
        curr.color = 'black'
    return cycle


def traverse(node):
    stack = []
    parent = node
    stack.append(node.id)
    node = node.parent
    while node != parent:
        stack.append(node.id)
        node = node.parent
    stack.append(node.id)
    while stack:
        print stack.pop()

g = create_graph()
all_vertices = g.get_all_vertices()

for vertex in all_vertices:
    vertex.color = 'white'
    vertex.parent = None

cycle = False

for start in all_vertices:
    if has_cycle(start, g):
        cycle = True
        break

if cycle:
    print "Cycle"
else:
    print "No Cycle"
