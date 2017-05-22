class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_children(self):
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children

    def __str__(self):
        return str(self.data)


def check_sum(arr):
    prev_sums_dict = {}
    running_sum = 0
    count = 0
    for index, item in enumerate(arr):
        prev_sums_dict[running_sum] = index
        running_sum += item
        if running_sum-k in prev_sums_dict:
            print arr[prev_sums_dict[running_sum-k]:index+1]
            count += 1


def visit(node):
    stack = []
    while node:
        stack.append(node.data)
        node = node.parent
    stack.reverse()
    check_sum(stack)


def dfs(root):
    if len(root.get_children()) == 0:
        visit(root)
    for child in root.get_children():
        child.parent = root
        dfs(child)


root = Node(5)
root.left = Node(-3)
root.right = Node(4)
root.left.left = Node(0)
root.left.right = Node(1)
root.left.left.left = Node(1)
root.left.left.left.left = Node(-1)
root.left.left.left.right = Node(2)
root.left.left.left.left.left = Node(2)
root.left.left.left.right.right = Node(5)
root.left.left.left.right.right.right = Node(-1)

root.right.left = Node(3)
root.right.right = Node(2)
root.right.right.left = Node(0)
root.right.right.right = Node(-9)
root.right.right.right.right = Node(0)

root.parent = None

k = 2

dfs(root)

