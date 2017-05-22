class MinHeap(object):

    def __init__(self):
        self.heap = []

    def get_parent(self, child):
        child += 1
        parent = child / 2
        parent -= 1
        if parent >= 0:
            return parent

    def get_left_child(self, parent):
        parent += 1
        child = parent * 2
        child -= 1
        if child < len(self.heap):
            return child

    def get_right_child(self, parent):
        parent += 1
        child = parent * 2 + 1
        child -= 1
        if child < len(self.heap):
            return child

    def swap(self, parent, child):
        temp = self.heap[parent]
        self.heap[parent] = self.heap[child]
        self.heap[child] = temp

    def bubble_up(self, child):
        parent = self.get_parent(child)
        while parent is not None:
            if self.heap[parent] > self.heap[child]:
                self.swap(parent, child)
                child = parent
                parent = self.get_parent(child)
            else:
                break

    def bubble_down(self, parent):
        min_child = self.get_left_child(parent)
        while min_child is not None:
            right_child = self.get_right_child(parent)
            if right_child:
                if self.heap[right_child] < self.heap[min_child]:
                    min_child = right_child
            if self.heap[min_child] < self.heap[parent]:
                self.swap(parent, min_child)
                parent = min_child
                min_child = self.get_left_child(parent)
            else:
                break

    def add_element(self, element):
        self.heap.append(element)
        self.bubble_up(len(self.heap)-1)

    def get_min(self):
        if len(self.heap) != 0:
            return self.heap[0]

    def remove_min(self):
        if len(self.heap) != 0:
            min_elem = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap = self.heap[:-1]
            self.bubble_down(0)
            return min_elem

    def heapify(self, elem_list):
        pass

    def min_heapify_node(self, element):
        pass

    def __str__(self):
        return str(self.heap)

h = MinHeap()
h.add_element(2)
print h
h.add_element(5)
print h
h.add_element(1)
print h
h.add_element(6)
print h
h.add_element(3)
print h
h.add_element(0)
print h
h.remove_min()
print h
h.remove_min()
print h