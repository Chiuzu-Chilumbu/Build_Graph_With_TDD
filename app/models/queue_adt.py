"""implementation of the queue ADT using a Python deque"""
from collections import deque


class Queue:
    def __init__(self, capacity):
        #  ensure the capacity is of integer type
        if not isinstance(capacity, int):
            raise TypeError('The queue capacity must be of type int')
        else:
            self.queue = deque()
            self.capacity = capacity

    def enqueue(self, item):
        """
        Add data to the end of the queue.
        Params -> Data: any Python data type, e.g., int, str, etc.
        """
        if self.isFull():
            raise Exception('Queue is Full')
        else:
            self.queue.append(item)

    def dequeue(self):
        """Remove data from the queue"""
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            self.queue.popleft()

    def size(self):
        return len(self.queue)
    

    def isEmpty(self):
        return len(self.queue) == 0
    

    def isFull(self):
        return len(self.queue) == self.capacity
    
    def show(self):
        print(self.queue)


    def peek(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.queue[0]
    
    def get_queue(self):
        return self.queue.copy()