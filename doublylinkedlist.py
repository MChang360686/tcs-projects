class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev

    def __str__(self):
        return f"prev: {self.prev}, data: {self.data}, next: {self.next}"
    

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, new_head_node):
        self.head = new_head_node.data

    def set_tail(self, new_tail_node):
        self.tail = new_tail_node.data

    def forward_traversal(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def backward_traversal(self):
        current = self.tail

        while current is not None:
            print(current.data)
            current = current.prev

    def get_len(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count
    
    def insert(self, new_node, prev_node):
        pass


    