"""implementation of the stack data structure"""

class Stack:
    """Implementation of Stack abstract data type"""

    def __init__(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError('Stack Capacity must be an integer')

        self.capacity = capacity
        self.stack = []

    def push(self, data):
        """
        Add data to top of stack
        Params -> Data : any python data type e.g. int, str e.t.c.
        """
        if len(self.stack) == self.capacity:
            raise Exception('Stack is full')
        else:
            self.stack.append(data)

    def pop(self):
        """Remove and return top most element in stack"""
        if len(self.stack) == 0:
            raise IndexError('cannot pop from empty stack')
        else:
            removed_item = self.stack.pop()
        return removed_item

    def size(self):
        """ Return size of stack"""
        return len(self.stack)

    def peek(self):
        """ Return top most element in stack"""
        return self.stack[-1]

    def isEmpty(self):
        """ Return True if stack is empty else return False"""
        return self.stack == []

    def isFull(self):
        """ Return True if stack is full else return False"""
        return len(self.stack) == self.capacity
