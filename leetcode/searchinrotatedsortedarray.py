import random

nums = [5, 8, 19, 20, 43, 24, 42]

print(nums[3])
print(nums[2:6])
print(nums[::2])

a = 'beans'
print(a[::-1])
print(nums[::-1])

def slice_list():
    return nums[random.randint(0, 3):random.randint(4, 7)]

print(slice_list())