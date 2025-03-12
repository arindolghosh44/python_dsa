class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"


    def is_empty(self):

        return   len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)



# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack size:", s.size())  # Output: 3
print("Top element:", s.peek())  # Output: 30
print("Popped:", s.pop())  # Output: 30
print("Stack after pop:", s.stack)  # Output: [10, 20]



###using deque
""""
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty"

    def is_empty(self):
        return not self.stack

    def size(self):
        return len(self.stack)

# Example usage
s = Stack()
s.push(5)
s.push(15)
print(s.pop())  # Output: 15"""
