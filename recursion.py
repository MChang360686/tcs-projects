
def print_numbers(num_start, num_end):
    if num_start == num_end:
        print(num_start)
    else:
        print(num_start)
        print_numbers(num_start + 1, num_end)

print_numbers(0, 10)