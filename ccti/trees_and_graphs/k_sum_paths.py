class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


sum = 5

root = Node(1)

root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(1)

root.right = Node(-1)
root.right.left = Node(4)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right = Node(5)
root.right.right.right = Node(6)


def get_key(node):
    return node.key


def visit(node):
    path_arr = []
    while node:
        path_arr.append(node.key)
        node = node.parent
    path_arr.reverse()
    return path_arr


def print_sum(arr, sum):
    running_sum_set = set()
    curr_sum = 0
    running_sum_set.add(curr_sum)
    for elem in arr:
        curr_sum += elem
        if (curr_sum-sum) in running_sum_set:
            print "+1", arr
        running_sum_set.add(curr_sum)


def k_sum_paths(start):
    if not hasattr(start, 'parent'):
        start.parent = None
    if not start.left and not start.right:
        arr = visit(start)
        print_sum(arr, sum)
    children = []
    if start.left:
        children.append(start.left)
    if start.right:
        children.append(start.right)
    for child in children:
        child.parent = start
        k_sum_paths(child)


k_sum_paths(root)

