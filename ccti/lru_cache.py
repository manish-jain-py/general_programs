class Node:

    def __init__(self, key):
        self.data = key
        self.prev_node = None
        self.next_node = None

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0
        self.max_length = 6

    def add_node(self, key):
        new_node = Node(key)
        if not self.head:
            self.head = new_node
            self.end = new_node
        else:
            self.end.next_node = new_node
            new_node.prev_node = self.end
            self.end = new_node
        self.length += 1
        return new_node

    def remove_node(self):
        removed_key = self.head.data
        if self.length == 1:
            self.head = None
            self.end = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
        self.length -= 1
        return removed_key

    def __str__(self):
        curr = self.head
        return_str = ''
        while curr is not None:
            return_str += str(curr.data) + ","
            curr = curr.next_node
        return return_str

class lru:

    def __init__(self):
        self.lru_dict = {} # key's value will be a list of two items - 1. value provided 2. LinkedList Node reference
        self.lru_list = LinkedList()

    def get(self, key):

        # if key is present in the dict, get node ref from key, and move it to front
        key_val = self.lru_dict.get(key, None)
        if key_val:
            node = key_val[1]
        else:
            node = None

        if node:
            self.move_to_front(node)
            return key_val[0]
        else:
            return None

    def put(self, key, val):
        if key not in self.lru_dict:
            if self.lru_list.length == self.lru_list.max_length:
                removed_key = self.lru_list.remove_node()
                self.lru_dict.pop(removed_key)
            new_node = self.lru_list.add_node(key)
            self.lru_dict[key] = [val, new_node]
        else:
            self.lru_dict[key][0] = val
            existing_node = self.lru_dict[key][1]
            self.move_to_front(existing_node)
        return self.lru_list.head

    def move_to_front(self, node):
        if self.lru_list.length > 1 and self.lru_list.end != node:
            if node.prev_node:
                node.prev_node.next_node = node.next_node
            if node.next_node:
                node.next_node.prev_node = node.prev_node
            self.lru_list.end.next_node = node
            node.prev_node = self.lru_list.end
            node.next_node = None
            self.lru_list.end = node


# Testing the LRU
new_lru = lru()
print new_lru.lru_list
new_lru.put('a', 100)
print new_lru.lru_list
new_lru.put('b', 10)
print new_lru.lru_list
new_lru.put('c', 1)
print new_lru.lru_list
new_lru.put('d', 1000)
print new_lru.lru_list
new_lru.put('e', 90)
print new_lru.lru_list
new_lru.put('f', 110)
print new_lru.lru_list
new_lru.put('g', 1110)
print new_lru.lru_list
print new_lru.get('e')
print new_lru.lru_list
print new_lru.get('e')
print new_lru.lru_list
new_lru.put('f', 10)
print new_lru.get('f')
print new_lru.lru_list