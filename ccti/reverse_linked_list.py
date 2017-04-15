from LinkedList import LinkedList

ll = LinkedList()
ll.add_node('a')
ll.add_node('b')
ll.add_node('c')
ll.add_node('d')
print ll.find_node('b')


def reverse_list(link_list):
    curr = link_list.head
    link_list.head = link_list.tail
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev

        prev = curr
        curr = next_node
        if curr:
            link_list.tail = curr

    return link_list.head

print reverse_list(ll)
