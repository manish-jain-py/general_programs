from LinkedList import LinkedList

ll = LinkedList()
a = ll.add_node('a')
b = ll.add_node('b')
c = ll.add_node('c')
d = ll.add_node('d')
e = ll.add_node('e')
f = ll.add_node('f')
g = ll.add_node('g')

#print c

def del_node(d):
    curr = d
    next = d.next
    while next:
        curr.key = next.key
        curr.next = next.next
        curr = curr.next
        next = next.next

print ll
del_node(e)
print ll




