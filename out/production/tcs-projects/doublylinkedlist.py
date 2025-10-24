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
    
    def insert(self, new_node, prev, next):
        new = Node(new_node)

        if self.head is None:
            self.head = new
            self.tail = new
        elif prev is None:
            new.set_next(self.head)
            self.head.set_prev(new)
            self.head = new
        elif next is None:
            current = self.tail
            self.tail = new
            current.set_next(new)
            new.set_prev(current)
        else:
            current = self.head

            while current != None:
                if current.data == prev and current.next.data == next:
                    new.set_next(current.next)
                    new.set_prev(current)

                    current.next.set_prev(new)
                    current.set_next(new)
                else:
                    current = current.next
                     

            
l = DoublyLinkedList()
l.insert(1, None, None)
l.insert(2, 1, None)
l.insert(8, None, 1)
l.insert(5, 1, 2)
l.forward_traversal()
