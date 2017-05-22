class MaxHeap:

    def __init__(self):
        self.heap = []
        self.heap_size = len(self.heap)

    def get_parent(self, i):
        if i == 0:
            return None
        i += 1
        return i/2 - 1

    def get_left_child(self, i):
        i += 1
        left = 2 * i - 1
        if left < (self.heap_size - 1):
            return left

    def get_right_child(self, i):
        i += 1
        right = 2 * i
        if right < self.heap_size - 1:
            return right

    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def bubble_up(self, i):
        parent = self.get_parent(i)
        if parent is not None:
            if self.heap[parent] < self.heap[i]:
                self.swap(parent, i)
                self.bubble_up(parent)

    def bubble_down(self, i):
        largest = i
        left = self.get_left_child(i)
        if left:
            if self.heap[left] > self.heap[largest]:
                largest = left

            right = self.get_right_child(i)
            if right:
                if self.heap[right] > self.heap[largest]:
                    largest = right

            if largest != i:
                self.swap(largest, i)
                self.bubble_down(largest)

    def insert(self, item):
        self.heap.append(item)
        self.heap_size += 1
        self.bubble_up(self.heap_size-1)

    def extract_max(self):
        if self.heap_size > 0:
            max = self.heap[0]
            if self.heap_size > 1:
                self.heap[0] = self.heap[self.heap_size - 1]
                del(self.heap[self.heap_size - 1])
                self.heap_size -= 1
                self.bubble_down(0)
            else:
                self.heap = []
                self.heap_size = 0
            return max

    def build_max_heap(self, arr):
        self.heap = []
        self.heap_size = 0
        for item in arr:
            self.insert(item)
        last_non_leaf = self.heap_size/2 + 1
        for i in range(last_non_leaf, 0, -1):
            self.bubble_down(i)

    def heap_sort(self, arr):
        self.build_max_heap(arr)
        size = self.heap_size
        new_arr = [None for i in range(size)]
        if self.heap_size > 1:
            for i in range(size - 1, -1, -1):
                maximum = self.extract_max()
                new_arr[i] = maximum
            return new_arr

    def __str__(self):
        return str(self.heap)

hp = MaxHeap()
hp.build_max_heap([30, 5, 10, 15, 50, 35, 40])
hp.extract_max()
print hp.heap_sort([30, 55, 5, 10, 15, 50, 35, 40])



