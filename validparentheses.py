string = "()[{{}}]"

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
  
s = Stack()

def solution(string):
    for p in string:
        print(p)
        match(p):
            case "(":
                s.push("(")
            case ")":
                last = s.peek()
                if last == "(":
                    s.pop()
                    continue
                else:
                    return False
            case "{":
                s.push("{")
            case "}":
                last = s.peek()
                if last == "{":
                    s.pop()
                    continue
                else:
                    return False
            case "[":
                s.push("[")
            case "]":
                last = s.peek()
                if last == "[":
                    s.pop()
                    continue
                else:
                    return False
    return True

print(solution(string))