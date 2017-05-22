class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data) + "->" + str(self.next)


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        return new_node

    def __str__(self):
        return str(self.head)


ll = LinkedList()

ll.add_node(4)
ll.add_node(7)
middle = ll.add_node(5)
ll.add_node(1)
middle = ll.add_node(9)

print ll


def remove_middle(middle):
    prev = None
    while True:
        if middle.next is None:
            if prev:
                prev.next = None
                break
            else:
                print "can't be deleted"
                return False
        else:
            middle.data = middle.next.data
            prev = middle
            middle = middle.next


remove_middle(middle)
print ll

