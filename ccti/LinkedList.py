class Node:

    def __init__(self, key):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key) + "->" + str(self.next)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def add_node(self, key):

        n = Node(key)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        return n

    def find_node(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None
