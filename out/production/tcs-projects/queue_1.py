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
        return self.queue[-1]
    
q = Queue()


q.enqueue(3)
q.enqueue(5)
q.enqueue(3)
q.dequeue()
print(q.queue)

class QueueStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def is_empty(self):
        if len(self.q1) == 0 and len(self.q2) == 0:
            return True
        else:
            return False
        
    def push(self, item):
        self.q2.append(item)

        for item in self.q1:
            self.q2.append(item)
            self.q1.pop(0)

        temp = self.q1
        self.q2 = self.q1
        self.q1 = temp

    def pop_stack(self):
        last = self.q1[0]
        self.q1.pop(0)
        return last
    
qs = QueueStack()

qs.push(1)
qs.push(2)
qs.push(3)
print(qs.q1)
print(qs.pop_stack())
