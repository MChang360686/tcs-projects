# https://leetcode.com/problems/reverse-linked-list/
ll = [1, 2, 3, 4, 5]

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return 'stack is empty'
        else:
            return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def get_length(self):
        return len(self.stack)

class Solution:
    def reverse_list(self, head):
        stack = Stack()
        for item in head:
            stack.push(item)
        reverse = []
        while stack.get_length() > 0:
            reverse.append(stack.peek())
            stack.pop()
        return reverse

s = Solution()
print(s.reverse_list(ll))