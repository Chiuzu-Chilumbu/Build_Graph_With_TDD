class Stack:
    """Implementation of Stack abstract data type"""

    def __init__(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError('Stack Capacity must be an integer')

        self.capacity = capacity
        self.stack = []

    def push(self, data):
        if len(self.stack) == self.capacity:
            raise Exception('Stack is full')
        self.stack.append(data)
        return self.stack

    def pop(self):
        if not self.stack:
            raise IndexError('Cannot pop from empty stack')
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.stack:
            raise Exception('Stack is empty')
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity
    
    def get_stack(self):
        return self.stack.copy()  # Return a copy to avoid mutation
