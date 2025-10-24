h = [1,8,6,2,5,4,8,3,7]

def naive(height):
    max_sum = 0
    for i in range(0, len(height)):
        val = height[i]
        for j in range(i + 1, len(height)):
            if val > height[j]:
                area = height[j] * (j - i)
            else:
                area = val * (j - i)
            if area > max_sum:
                max_sum = area
    return max_sum

def better(height):
    start = 0
    end = len(height) - 1
    max_water = 0

    while start != end:
        if height[start] > height[end]:
            if (height[end] * (end - start)) > max_water:
                max_water = (height[end] * (end - start))
            end -= 1
        else:
            if (height[start] * (end - start)) > max_water:
                max_water = (height[start] * (end - start))
            start += 1

    return max_water

print(better(h))
print(naive(h))