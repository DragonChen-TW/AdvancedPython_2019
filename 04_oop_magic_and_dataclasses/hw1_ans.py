class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let's do a linked-list version stack
# Functions: push, pop, is_empty
class Stack:
    def __init__(self):
        self.head = None

    def push(self, n):
        new_node = Node(n)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head.next:      # just one node in Stack
            temp = self.head
            self.head = None
        else:                       # more than one
            temp = self.head
            self.head = self.head.next

        return temp.val

    def is_empty(self):
        return self.head is None

# Stack test script
l = [1, 3, 5]
s = Stack()
for n in l:
    s.push(n)

s.pop()
s.push('a')
s.push('b')
s.pop()

while not s.is_empty():
    print('{} > '.format(s.pop()),end='')
print()
# ans is 'a > 3 > 1 >'
# it is
