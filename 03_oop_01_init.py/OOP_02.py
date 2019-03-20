# Let's do a stack

class Stack:
    def __init__(self, max_len=100):
        self.array = []
        self.max_len = max_len

    def push(self, n):
        if self.is_full():
            print('ERROR, stack is full')
        else:
            self.array.append(n)

    def pop(self):
        return self.array.pop()

    def is_full(self):
        return len(self.array) >= self.max_len

    def is_empty(self):
        return len(self.array) == 0

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n1 = Node(1)
n2 = Node(3)
n3 = Node(5)
n1.next = n2
n2.next = n3

class Stack:
    def __init__(self):
        pass


l = [1, 3, 5]
s = Stack()
for n in l:
    s.push(n)

s.pop()
s.push('a')
s.push('b')
s.pop()

while not s.is_empty():
    last = s.pop()
    print(last)
