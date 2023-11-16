import numpy as np

class CircularQueue:
    def __init__(self, size):
        """The queue does not erase values ​​but rather overwrites them in practice"""
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
            # Check on which side the start and end are
            if self.end == self.size - 1:
                #[6, 2, 3, 4, 5]
                # In this case, the index of the last element (5) is equal to 4, so the if statement compares
                # if the final index 4 is equal to the total size - 1: 4 == 5-1
                # If this condition is met, it means that the queue has been linearly filled and is not full
                # Therefore, there are empty positions at the beginning of the queue
                # Thus, the index indicated for the next element becomes -1
                self.end = -1

            self.end +=1 # In this line, we add -1 + 1 to indicate index 0 of the queue, i.e., the beginning of it
            self.values[self.end] = value # Add the value to the queue
            self.elements +=1 # Update the number of elements
    
    def dequeue(self):
        if self.__empty():
            print('The queue is already empty')
            return 
        tmp = self.values[self.start] # Temporarily stores the value of the element to be removed
        self.start +=1 # Increment the start index to point to the next element
        if self.start == self.size -1:
            self.start = 0 # If start is at the end of the array, set to 0 (circular queue)
        self.elements -= 1 # Update the number of elements
        return tmp # Returns the removed value
    
    def first(self):
        if self.__empty():
            return -1
        return self.values[self.start]

queue = CircularQueue(5)
print(queue.first()) # Empty queue

for i in range(5):
    queue.enqueue(i)
print(f"The value of the first element is: {queue.first()}")

for j in range(2):
    print(f"The removed element has the value of {queue.dequeue()}")
print(f"The first element of the queue is: {queue.first()}")

for i in range(6,8):
    # The first iteration reverses the position of the indicators
    queue.enqueue(i)

for j in range(2):
    print(f"The removed element has the value of {queue.dequeue()}")
print(f"The first element of the queue is: {queue.first()}")
