import numpy as np

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.start = 0
        self.end = -1
        self.elements = 0
        self.values = np.empty(self.size, dtype=int)

    def __empty(self):
        return self.elements == 0
    
    def __is_full(self):
        return self.elements == self.size
    
    def enqueue(self, value):
        if self.__is_full():
            print('The queue is full')
            return
        else:
            #verificamos em qual lado está o start e o end
            if self.end == self.size - 1:
                self.end = -1
            self.end +=1
            self.values[self.end] = value
            self.elements +=1
    
    def dequeue(self):
        if self.__empty():
            print('The queue is already empty')
            return 
        tmp = self.values[self.start]
        self.start +=1
        if self.start == self.size:
            self.start = 0
        self.elements -= 1
        return tmp
    
    def first(self):
        if self.__empty():
            return -1
        return self.values[self.start]

queue = CircularQueue(5)
print(queue.first())

queue.enqueue(1)
print(queue.first())

queue.enqueue(2)
print(queue.first())

queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

queue.dequeue()
queue.dequeue()

print(queue.first())