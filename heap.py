class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def get_parent(self, index):
        return (index - 1)//2
    
    def get_right_child(self, index):
        return 2 * index + 2
    
    def get_left_child(self, index):
        return 2 * index + 1
    
    def has_parent(self, index):
        return self.get_parent(index) >= 0
    
    def has_left_child(self, index):
        return self.get_left_child(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child(index) < len(self.heap)
    
    def add_min(self, num):
        self.heap.append(num)
        i = len(self.heap) - 1
        while i != 0  and self.heap[self.get_parent(i)] > self.heap[i]:
            self.heap[self.get_parent(i)], self.heap[i] = self.heap[i], self.heap[self.get_parent(i)]
            i = self.get_parent(i)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        if len(self.heap) > 0:
            self.heapify(0)
        return root

    def heapify(self, index):
        smallest = index
        left_child = self.get_left_child(index)
        right_child = self.get_right_child(index)
        if self.has_left_child(index) and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        if self.has_right_child(index) and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def build_heap(self, elements):
        self.heap = elements
        for i in range(len(elements)//2 - 1, -1, -1):
            self.heapify(i)
    
# Create an object of MinHeap
# min_heap = MinHeap()

# # Add elements to the heap
# min_heap.add_min(4)
# print(min_heap.heap)

# min_heap.add_min(10)
# print(min_heap.heap)

# min_heap.add_min(3)
# print(min_heap.heap)

# min_heap.add_min(5)
# print(min_heap.heap)

# # Build the heap from a list of elements
# min_heap.build_heap([9, 7, 2, 1, 8])
# print(min_heap.heap)

# # Remove elements from the heap
# removed_element = min_heap.remove()
# print(f"Removed element: {removed_element}")
# print(min_heap.heap)

# removed_element = min_heap.remove()
# print(f"Removed element: {removed_element}")
# print(min_heap.heap)

class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def get_parent(self, index):
        return (index - 1)//2
    
    def get_right_child(self, index):
        return 2 * index + 2
    
    def get_left_child(self, index):
        return 2 * index + 1
    
    def has_parent(self, index):
        return self.get_parent(index) >= 0
    
    def has_left_child(self, index):
        return self.get_left_child(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child(index) < len(self.heap)
    
    def add(self, num):
        self.heap.append(num)
        i = len(self.heap) - 1
        while i != 0  and self.heap[self.get_parent(i)] < self.heap[i]:
            self.heap[self.get_parent(i)], self.heap[i] = self.heap[i], self.heap[self.get_parent(i)]
            i = self.get_parent(i)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        if len(self.heap) > 0:
            self.heapify(0)
        return root

    def heapify(self, index):
        smallest = index
        left_child = self.get_left_child(index)
        right_child = self.get_right_child(index)
        if self.has_left_child(index) and self.heap[smallest] < self.heap[left_child]:
            smallest = left_child
        if self.has_right_child(index) and self.heap[smallest] < self.heap[right_child]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def build_heap(self, elements):
        self.heap = elements
        for i in range(len(elements)//2 - 1, -1, -1):
            self.heapify(i)

# Create a MaxHeap object
max_heap = MaxHeap()

# Add elements to the heap
elements_to_add = [4, 10, 3, 5, 1]
for num in elements_to_add:
    max_heap.add(num)
    print(f"After adding {num}: {max_heap.heap}")

# Remove elements from the heap
while len(max_heap.heap) > 0:
    removed_element = max_heap.remove()
    print(f"After removing {removed_element}: {max_heap.heap}")

# Build a max heap from a list of elements
elements_to_build_heap = [7, 2, 8, 1, 6]
max_heap.build_heap(elements_to_build_heap)
print(f"After building max heap: {max_heap.heap}")