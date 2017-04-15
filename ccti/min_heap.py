class minheap(object):

    def __init__(self):
        self.elements = []

    def add(self, item):
        self.elements.append(item)
        item_index = len(self.elements)-1
        self.bubble_up(item_index)

    def remove_min(self):
        min_element = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.bubble_down(0)
        return min_element

    def bubble_up(self, child_index):
        parent_index = self.get_parent(child_index)
        while parent_index is not None:
            if self.elements[parent_index] > self.elements[child_index]:
                self.swap(parent_index, child_index)
                child_index = parent_index
                parent_index = self.get_parent(child_index)
            else:
                break

    def bubble_down(self, parent_index):
        left_child_index = self.get_left_child(parent_index)
        right_child_index = self.get_right_child(parent_index)
        while left_child_index is not None or right_child_index is not None:
            if left_child_index and right_child_index:
                if (self.elements[parent_index] > self.elements[left_child_index]) or (self.elements[parent_index] > self.elements[right_child_index]):
                    if self.elements[left_child_index] < self.elements[right_child_index]:
                        self.swap(parent_index, left_child_index)
                        parent_index = left_child_index
                    else:
                        self.swap(parent_index, right_child_index)
                        parent_index = right_child_index
            elif left_child_index and self.elements[parent_index] > self.elements[left_child_index]:
                self.swap(parent_index, left_child_index)
                parent_index = left_child_index
            elif right_child_index and self.elements[parent_index] > self.elements[right_child_index]:
                self.swap(parent_index, right_child_index)
                parent_index = right_child_index
            else:
                break
            left_child_index = self.get_left_child(parent_index)
            right_child_index = self.get_right_child(parent_index)

    def get_left_child(self, parent_index):
        parent_index += 1
        if parent_index*2 < len(self.elements):
            return (parent_index * 2) - 1

    def get_right_child(self, parent_index):
        parent_index += 1
        if ((parent_index*2)+1) < len(self.elements):
            return (parent_index*2)

    def get_parent(selfself, child_index):
        if child_index >= 1:
            child_index += 1
            return (child_index/2)-1

    def swap(self, x, y):
        temp = self.elements[x]
        self.elements[x] = self.elements[y]
        self.elements[y] = temp

    def __str__(self):
        return str(self.elements)

heap = minheap()

heap.add(5)
print heap
heap.add(3)
print heap
heap.add(15)
print heap
heap.add(1)
print heap
heap.add(0)
print heap
print heap.remove_min()
print heap
print heap.remove_min()
print heap
