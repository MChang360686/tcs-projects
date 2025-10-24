class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, key):
        self.heap.append(key)  # Add the key to the end of the heap
        self._heapify_up(len(self.heap) - 1)  # Restore the heap property

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            # Swap with the parent if the current node is smaller
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()

        # Replace root with the last element and remove the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)  # Restore the heap property
        return root

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Find the smallest among index, left child, and right child
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # Swap and continue heapifying if the smallest is not the current index
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)

    def peek_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def __str__(self):
        return str(self.heap)



min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)

print("Heap after inserts:", min_heap)
print("Minimum value:", min_heap.extract_min())
print("Heap after extracting min:", min_heap)
