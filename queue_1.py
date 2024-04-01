class Queue:

    def __init__ (self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[len(self.queue) - 1]
    
q = Queue()


q.enqueue(3)
q.enqueue(5)
q.enqueue(3)
q.dequeue()
print(q.queue)
