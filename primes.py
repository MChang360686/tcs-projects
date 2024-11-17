
def find_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True
        
print(find_prime(13))

class Grid:
    def __init__(self, length, width):
        self.grid = [[], [], []]
        for i in range(length):
            for j in range(width):
                self.grid[i].append(0)

    def print_grid(self):
        for i in range(3):
            print(self.grid[i])

    def mark_hit(self, x, y):
        self.grid[x][y] = 1

    