#https://leetcode.com/problems/combinations/description/

n = 4
k = 2

"""
Iterative Approach
"""

def iter_solution(n, k):
    output = []
    for i in range(1, n+1):
        sublist = []
        j = i
        while len(sublist) < k:
            sublist.append(j)
            j+=1
            print(sublist)
        output.append(sublist)

    return output

print(iter_solution(n, k))

def iter_fib(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, b)
        c = a + b
        a = b
        b = c

def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)


iter_fib(10)
print(recur_fib(10))

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)
    
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
    

print(recursive_sum(10))
print(recursive_factorial(10))

        

