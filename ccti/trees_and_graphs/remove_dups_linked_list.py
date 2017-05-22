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


def remove_dup(ll):
    d = set()
    node = ll.head
    prev = None
    while node:
        if node.data in d:
            # print node
            # print prev
            prev.next = node.next
        else:
            d.add(node.data)
            prev = node
        node = node.next
    print ll


def remove_dup_without_extra_buffer(ll):
    node = ll.head

    while node:

        next_node = node.next
        prev = node

        while next_node:
            if next_node.data == node.data:
                prev.next = next_node.next
            else:
                prev = next_node
            next_node = next_node.next

        node = node.next

    print ll

ll = LinkedList()

ll.add_node(4)
ll.add_node(4)
ll.add_node(4)
ll.add_node(4)
ll.add_node(4)
ll.add_node(4)
ll.add_node(4)
ll.add_node(4)
ll.add_node(7)
ll.add_node(5)
ll.add_node(1)
ll.add_node(9)
ll.add_node(7)
ll.add_node(4)
ll.add_node(3)
ll.add_node(3)
ll.add_node(3)
ll.add_node(3)
ll.add_node(2)
ll.add_node(1)
ll.add_node(4)
ll.add_node(4)
ll.add_node(7)
ll.add_node(5)
ll.add_node(1)
ll.add_node(9)
ll.add_node(7)
ll.add_node(4)
ll.add_node(3)
ll.add_node(2)
ll.add_node(1)
ll.add_node(1)

print ll.head

remove_dup_without_extra_buffer(ll)