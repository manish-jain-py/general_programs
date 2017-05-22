from LinkedList import LinkedList


def sort_by_element(link_list, elem):
    ll_less_than_elem = LinkedList()
    ll_more_than_elem = LinkedList()
    curr = link_list.head
    while curr is not None:
        if curr.key < elem:
            ll_less_than_elem.add_node(curr.key)
        else:
            ll_more_than_elem.add_node(curr.key)
        curr = curr.next

    ll_less_than_elem.tail.next = ll_more_than_elem.head
    ll_less_than_elem.tail = None
    print ll_less_than_elem

link_list = LinkedList()

link_list.add_node(10)
link_list.add_node(12)
link_list.add_node(5)
link_list.add_node(3)
link_list.add_node(8)
link_list.add_node(11)
link_list.add_node(14)
link_list.add_node(12)
link_list.add_node(4)
link_list.add_node(1)

sort_by_element(link_list, 5)