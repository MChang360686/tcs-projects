

grid = [['', '', ''], ['', '', ''], ['', '', '']]

def print_grid(arr):
    for a in arr:
        print(a)

#print_grid(grid)
        
while True:
    print_grid(grid)

    y_coordinate = int(input("Please enter a y-cordinate (0-2) "))
    x_coordinate = int(input("Please enter a x coordinate (0-2) "))

    s = input("Please enter either an x or o ")

    grid[y_coordinate][x_coordinate] = s