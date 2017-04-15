class BTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return "{ " + str(self.left) + "<--" + str(self.data) + "-->" + str(self.right) + "}"


def dfs(root, node, found=None):
    for child in [root.left, root.right]:
        if child:
            child.parent = root
            if child == node:
                return child
            else:
                found = dfs(child, node)
                if found:
                    return found


def traverse(node, stack=[]):
    while node:
        stack.append(node.data)
        node = node.parent
    stack.reverse()
    return stack


def first_common_ancestor(root, node1, node2):
    lca = None
    path1 = traverse(dfs(root, node1), [])
    path2 = traverse(dfs(root, node2), [])
    len_path1 = len(path1)
    len_path2 = len(path2)
    for i in range(min(len_path1, len_path2)):
        if path1[i] == path2[i]:
            lca = path1[i]
    return lca


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

print first_common_ancestor(a, b, c)