from collections import deque

class MyDeque:
    def __init__(self):  # Constructor
        self.queue = deque()

    def appendFront(self, item):
        """Insert element at the front."""
        self.queue.appendleft(item)

    def appendEnd(self, item):
        """Insert element at the rear."""
        self.queue.append(item)

    def popLeft(self):
        """Remove and return element from the front."""
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def popRight(self):
        """Remove and return element from the rear."""
        if not self.is_empty():
            return self.queue.pop()
        return "Queue is empty"

    def front_peek(self):
        """Return the front element without removing it."""
        return self.queue[0] if not self.is_empty() else "Queue is empty"

    def rear_peek(self):
        """Return the rear element without removing it."""
        return self.queue[-1] if not self.is_empty() else "Queue is empty"

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the deque."""
        return len(self.queue)


# **USE CASES**  
d = MyDeque()

# **1. Inserting at the Front**
d.appendFront(1)
d.appendFront(2)
d.appendFront(3)
d.appendFront(4)
d.appendFront(5)
d.appendFront(6)
print("Deque after inserting at the front:", d.queue)  # deque([6, 5, 4, 3, 2, 1])

# **2. Inserting at the End**
d.appendEnd(10)
d.appendEnd(9)
d.appendEnd(8)
d.appendEnd(7)
print("Deque after inserting at the end:", d.queue)  # deque([6, 5, 4, 3, 2, 1, 10, 9, 8, 7])

# **3. Removing from the Front**
print("Popped from front:", d.popLeft())  # 6
print("Deque after popping from front:", d.queue)

# **4. Removing from the End**
print("Popped from rear:", d.popRight())  # 7
print("Deque after popping from rear:", d.queue)

# **5. Peek Front and Rear**
print("Front element:", d.front_peek())  # Should return 5
print("Rear element:", d.rear_peek())  # Should return 8

# **6. Checking Size and Empty Status**
print("Size of deque:", d.size())  # Should return 8
print("Is deque empty?", d.is_empty())  # Should return False

# **7. Removing all elements**
while not d.is_empty():
    print("Removing:", d.popLeft())

print("Is deque empty after removing all elements?", d.is_empty())  # Should return True
