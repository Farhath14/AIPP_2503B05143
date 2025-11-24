class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Insert an element on top of stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the top element of stack"""
        if self.is_empty():
            raise IndexError("Pop attempted on empty stack")
        return self.items.pop()

    def peek(self):
        """Return top element without removing it"""
        if self.is_empty():
            raise IndexError("Peek attempted on empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ---------- Testing ----------
s = Stack()

# edge case tests
try:
    s.pop()
except Exception as e:
    print("Pop edge case:", e)

try:
    s.peek()
except Exception as e:
    print("Peek edge case:", e)

# normal operations
s.push(10)
s.push(20)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Is empty:", s.is_empty())
