class Stack:
    def __init__(self):
        self.items = []

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
class Equation:
    def __init__(self):
        self.equation = ''

    def get_equation(self):
        return self.equation
    
    def conc_eq(self, new_char):
        self.equation += new_char

    def clear_eq(self):
        self.equation = ''


equations = []

def calculate_postfix(equation):
    stack = Stack()
    equation = equation.split()
    for char in equation:
        if char.isnumeric():
            stack.push(int(char))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            
            if char == '+':
                stack.push(num1 + num2)
            elif char == '-':
                stack.push(num1 - num2)
            elif char == '*':
                stack.push(num1 * num2)
            elif char == '/':
                stack.push(num1 / num2)

