class CircularScheduler:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")

        self.capacity = capacity
        self.array = [None] * capacity
        self.head = 0        
        self.tail = 0        
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def add_task(self, task: str) -> None:
        if self.is_full():
            raise OverflowError("Scheduler is full")

        self.array[self.tail] = task
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def remove_task(self) -> str:
        if self.is_empty():
            raise IndexError("No tasks to remove")

        task = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return task

    def get_next_task(self) -> str:
       
        if self.is_empty():
            raise IndexError("No tasks available")

        task = self.array[self.head]
        self.head = (self.head + 1) % self.capacity
        return task

    def peek(self) -> str:
        if self.is_empty():
            raise IndexError("No tasks available")
        return self.array[self.head]

    def __str__(self):
        return f"Scheduler({self.array}), head={self.head}, tail={self.tail}, size={self.size}"
    
if __name__ == "__main__":
    scheduler = CircularScheduler(3)

    scheduler.add_task("Task A")
    scheduler.add_task("Task B")
    scheduler.add_task("Task C")

    print("Initial state:")
    print(scheduler)

    print("\nRound Robin Execution:")
    for _ in range(6):
        print(scheduler.get_next_task())

    print("\nRemoving a task:")
    removed = scheduler.remove_task()
    print("Removed:", removed)

    print("\nCurrent State:")
    print(scheduler)