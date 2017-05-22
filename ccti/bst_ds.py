class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):

    def __init__(self):
        self.root = None

    def __insert__(self, data):
        if not self.root:
            self.root = Node(data)
        else:
