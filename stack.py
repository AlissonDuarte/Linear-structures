import numpy as np

class Stack:
    def __init__(self, size):
        """
        The user should not have access to other elements, only to the first.
        """
        self.__size = size
        self.__top = -1
        self.__values = np.empty(self.__size, dtype=int)

    def __is_full(self):
        """
        Used only when stacking new elements.
        Method with an underscore to indicate that it's private.
        """
        return self.__top == self.__size - 1

    def __is_empty(self):
        """
        Used to check if the stack is empty.
        """
        return self.__top == -1

    def push(self, value):
        """
        Adds a new element to the top of the stack.
        Raises an exception if the stack is full.
        """
        if self.__is_full():
            raise Exception("The stack is full")
        else:
            self.__top += 1
            self.__values[self.__top] = value
            return f"the value: {value} has been entered!"

    def pop(self):
        """
        Removes the top element from the stack.
        Raises an exception if the stack is empty.
        """
        if self.__is_empty():
            raise Exception("The stack is empty")
        else:
            self.__top -= 1
            return f"the value: {self.__values[self.__top]} has been removed"

    def peek_top(self):
        """
        Returns the top element of the stack.
        Returns -1 if the stack is empty.
        """
        if self.__top != -1:
            return self.__values[self.__top]
        else:
            return -1

# Example usage of the Stack class

stack = Stack(5)

for x in range(5):
    print(stack.push(x))
print("Top of stack is:", stack.peek_top())

for _ in range(6):
    print(stack.pop())
print("Top of stack is:", stack.peek_top())