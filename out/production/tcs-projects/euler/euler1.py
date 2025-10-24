def euler_naive():
    sum = 0
    for i in range(0, 1001):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

def euler_better():
    sum = 0
    for i in range(0, 1000, 3):
        sum += i

    for i in range(0, 1000, 5):
        sum += i

    for i in range(0, 1000, 15):
        sum -= i

    return sum

print(euler_naive())
print(euler_better())

# optimal solution
gauss_sum = lambda n: lambda m: m * ((n - 1) // m) * ((n - 1) // m + 1) // 2
gs = gauss_sum(1000)
print(gs(3) + gs(5) - gs(15))
