class BTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "{ " + str(self.left) + "<--" + str(self.data) + "-->" + str(self.right) + "}"

a = root = BTNode('A')
b = a.left = BTNode('B')
d = b.left = BTNode('D')
e = b.right = BTNode('E')
f = d.left = BTNode('F')
g = f.left = BTNode('G')
h = f.right = BTNode('H')
c = a.right = BTNode('C')
i = c.right = BTNode('I')
j = i.left = BTNode('J')
k = i.right = BTNode('K')


def inorder_successor(node, root):
    found = False
    set_parent(root)
    parent = node.parent
    if node.right:
        inorder(node.right)
        found = True
    else:
        while (not found) and parent is not None:
            if node == parent.left:
                print parent.data
                found = True
            else:
                node = parent
            parent = node.parent
    if not found:
        print "No successor"


def inorder(start):
    if start:
        if start.left:
            if inorder(start.left):
                return True
        print start.data
        return True


def set_parent(root, parent=None):
    if root:
        root.parent = parent
        if root.left:
            set_parent(root.left, root)
        if root.right:
            set_parent(root.right, root)

inorder_successor(d, a)

