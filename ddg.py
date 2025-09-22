import random

class CircularArray():
    def __init__(self):
        arr = []
        self.max_length = 10

    def get_next(self, current_index):
        if current_index == 9:
            return 0
        else:
            return current_index + 1

def d6():
    return random.randint(1, 6)

