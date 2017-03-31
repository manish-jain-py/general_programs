from collections import deque
from minimal_height_bst import create_min_bst

bst = create_min_bst([2, 3, 5, 7, 12, 14, 16, 21, 36, 40, 70, 100, 102])


class LinkedList:

    def __init__(self, data):
        self.data = data
        self.link = None

    def __str__(self):
        return str(self.data) + "->" + str(self.link)


def create_ll_from_bst(source):
    nodes_queue = deque()
    bst.level = 0
    nodes_queue.appendleft(bst)
    dict_linked_list = {}
    while len(nodes_queue) > 0:
        curr_node = nodes_queue.pop()
        ll = curr_node.data
        if dict_linked_list.get(curr_node.level):
            dict_linked_list[curr_node.level].append(ll)
        else:
            dict_linked_list[curr_node.level] = [ll]
        print curr_node.data, curr_node.level
        children = [curr_node.left, curr_node.right]
        for child in children:
            if child:
                child.level = curr_node.level + 1
                nodes_queue.appendleft(child)
    for key in dict_linked_list:
        head = None
        parent = None
        for item in dict_linked_list[key]:
            node = LinkedList(item)
            if parent:
                parent.link = node
            parent = node
            if head is None:
                head = node
        print head

    print dict_linked_list



create_ll_from_bst(bst)