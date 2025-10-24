
def get_hashes():
    input_one = input("Please enter the first hash").lower()
    input_two = input("Please enter the second hash").lower()

    return input_one, input_two

def check(a, b):
    if a == b:
        return True
    else:
        return False

a, b = get_hashes()
print(check(a, b))