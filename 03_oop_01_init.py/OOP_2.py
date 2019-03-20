# Let's do a stack

class Stack:
    def __init__(self, max_len=100):
        self.array = []
        self.max_len = 100

    def push(self, n):
        self.array.append(n)

    def pop(self):
        return self.array.pop()

    def is_full(self):
        return len(self.array) < self.max_len

    def is_empty(self):
        return len(self.array) == 0
