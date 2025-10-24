class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]
    
def longest_valid_parentheses(string):
    if len(string) == 0:
        return 0
    else:
        s = Stack()
        arr = []
        for i in range(0, len(string)):
            if string[i] == '(':
                s.push(tuple((i, '(')))
                arr.append(0)
            else:
                if s.peek()[1] == '(':
                    arr[s.peek()[0]] = 1
                    arr.append(1)
                else:
                    continue
        
        print(arr)

        longest = 0
        sum = 0
        for j in range(0, len(arr)):
            if arr[j] == 1:
                sum += 1
            else:
                if sum > longest:
                    longest = sum
                    sum = 0

        if sum > longest:
            longest = sum

        return longest
    
print(longest_valid_parentheses('()'))