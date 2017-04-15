from collections import deque

def BFS(start, g):
    nodes_queue = deque()
    nodes_queue.appendleft(start)
    while len(nodes_queue) != 0:
        curr_node = nodes_queue.pop()
        visit(curr_node)
        for child in curr_node.get_all_neighbors():
            child = g.get_vertex(child)
            if not child.visited:
                child.parent = curr_node
                nodes_queue.appendleft(child)


def visit(node):
    node.visited = True
    print str(node)


def visit_end(node, g):
    if node.parent:
        g.remove_edge(node.parent, node)
    return node.id
    print "end node: ", str(node.id)


def DFS(start, g, build_order=[]):
    if not hasattr(start, 'parent'):
        start.parent = None
    visit(start)
    children = [g.get_vertex(child) for child in start.get_all_neighbors()]
    if not children:
        end_node = visit_end(start, g)
        if end_node not in build_order:
            build_order.append(end_node)
    else:
        for child in children:
            child.parent = start
            DFS(child, g, build_order)
    return build_order






