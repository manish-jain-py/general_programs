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

    def __iter__(self):
        return self

    def next(self):
        if not self:
            raise StopIteration
        elif self.left:
            return self.left
        elif self.right:
            return self.right


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