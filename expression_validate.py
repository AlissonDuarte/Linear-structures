import numpy as np

class Stack:
    def __init__(self, size):
        self.__size = size
        self.__top = -1
        self.__values = np.chararray(self.__size, unicode=True)

    def __is_full(self):
        return self.__top == self.__size - 1

    def is_empty(self):
        return self.__top == -1

    def push(self, value):
        if self.__is_full():
            raise Exception("Stack is full")
        else:
            self.__top += 1
            self.__values[self.__top] = value

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        else:
            value = self.__values[self.__top]
            self.__top -= 1
            return value

    def peek_top(self):
        if not self.is_empty():
            return self.__values[self.__top]
        else:
            return None

def validate_expression(expression):
    stack = Stack(len(expression))

    for i in range(len(expression)):
        ch = expression[i]
        if ch in ['{', '[', '(']:
            stack.push(ch)
        elif ch in ['}', ']', ')']:
            if not stack.is_empty():
                chx = str(stack.pop())
                if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
                    raise Exception(f"Error: {ch} in position {i}")
    if not stack.is_empty():
        raise Exception("Error: Unmatched opening bracket(s)")

expression = input("Type your expression: ")
validate_expression(expression)
print("Expression is valid.")
