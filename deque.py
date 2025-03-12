from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):  # enqueue
        self.queue.append(item)

    def popL(self):  # dequeue from left
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def popR(self):  # dequeue from right
        if not self.is_empty():
            return self.queue.pop()  # Corrected from popright() to pop()
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


q = Queue()

q.push(1)
q.push(12)
q.push(13)
q.push(14)
q.push(15)
q.push(16)

print(q.popL())  # Corrected function call
print(q.popR())  # Corrected function call
print(q.queue)
