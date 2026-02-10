class Stack:

    def __init__(self):
        self.stack = []

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if self.empty():
            return "Stack is empty"
        else:
            return self.stack[0]

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        self.stack.pop(0)

s = Stack()
s.push(5)
print(s.stack)

def balanced_parentheses(string):
    s = Stack()
    print(string)

    for p in string:
        match(p):
            case "{":
                s.push(p)
            case "(":
                s.push(p)
            case "[":
                s.push(p)
            case "}":
                item = s.peek()
                if item == "{":
                    s.pop()
                    continue
                else:
                    return "Unbalanced"
            case ")":
                item = s.peek()
                if item == "(":
                    s.pop()
                    continue
                else:
                    return "Unbalanced"
            case "]":
                item = s.peek()
                if item == "[":
                    s.pop()
                    continue
                else:
                    return "Unbalanced"
            case _:
                print("Unknown symbol")
                break

    return "Balanced"

sequence = '{[([])]}'

print(balanced_parentheses(sequence))       
            