class PQ(object):

    def __init__(self):
        self.elements = []
        self.objects = []

    def __str__(self):
        return str(self.elements) + '\n' + str([str(obj) for obj in self.objects])

    def get_left_child(self, parent):
        parent += 1
        left_child = parent * 2
        left_child -= 1
        if left_child < len(self.elements):
            return left_child
        else:
            return None

    def get_right_child(self, parent):
        parent += 1
        right_child = parent * 2 + 1
        right_child -= 1
        if right_child < len(self.elements):
            return right_child
        else:
            return None

    def get_parent(self, child):
        child += 1
        parent = child/2
        parent -= 1
        if parent >= 0:
            return parent
        else:
            return None

    def get_min(self):
        if len(self.elements) > 0:
            return self.objects[0], self.elements[0]

    def swap(self, x, y):
        temp = self.elements[x]
        self.elements[x] = self.elements[y]
        self.elements[y] = temp
        temp = self.objects[x]
        self.objects[x] = self.objects[y]
        self.objects[y] = temp

    def bubble_up(self, child):
        while True:
            parent = self.get_parent(child)
            if parent is None:
                return
            else:
                if self.elements[parent] > self.elements[child]:
                    self.swap(parent, child)
                    child = parent
                else:
                    return

    def bubble_down(self, parent):
        while True:
            min_child = self.get_left_child(parent)
            if min_child is None:
                return
            else:
                right = self.get_right_child(parent)
                if right is not None:
                    if self.elements[right] < self.elements[min_child]:
                        min_child = right
                if self.elements[min_child] < self.elements[parent]:
                    self.swap(parent, min_child)
                    parent = min_child
                else:
                    return

    def min_heapify(self, new, prev):
        if self.elements[new] < prev:
            self.bubble_up(new)
        elif self.elements[new] > prev:
            self.bubble_down(new)

    def update_priority(self, element, new_priority):
        prev_priority = self.elements[element]
        self.elements[element] = new_priority
        self.min_heapify(element, prev_priority)

    def del_min(self):
        if len(self.elements) > 0:
            min_elem = self.elements[0]
            self.elements[0] = self.elements[-1]
            self.elements = self.elements[:-1]
            min_obj = self.objects[0]
            self.objects[0] = self.objects[-1]
            self.objects = self.objects[:-1]
            self.bubble_down(0)
            return min_elem, min_obj

    def add(self, elem, obj=None):
        self.elements.append(elem)
        self.objects.append(obj)
        self.bubble_up(len(self.elements)-1)


# class demo(object):
#
#     def __init__(self, key):
#         self.a = key
#
#     def __str__(self):
#         return str(self.a)
#
# a = demo(2)
# b = demo(5)
# c = demo(3)
# d = demo(1)
#
# pq = PQ()
# pq.add(2, a)
# print pq
# pq.add(5, b)
# print pq
# pq.add(3, c)
# print pq
# pq.add(1, d)
# print pq
# print pq.del_min()
# print pq
# print pq.del_min()
# print pq
