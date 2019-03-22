class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    now = head

    while now:
        print('{} > '.format(now.val),end='')
        now = now.next
    print() # print newline

# # Linked-list and print test
# n1 = Node(1)
# n2 = Node(3)
# n3 = Node(5)
# n1.next = n2
# n2.next = n3
#
# print_linked_list(n1)
# # expect 1 > 3 > 5 >

# Let's do a linked-list version stack
# Functions: push, pop, is_empty
class Stack:
    def __init__(self):
        self.head = None

    def push(self, n):
        # push n behind last one in self.head
        pass

    def pop(self):
        # pop last one in self.head
        return 0 # and return

    def is_empty(self):
        # check is linked-list empty
        return True # return bool True or False

# # Stack test script
# l = [1, 3, 5]
# s = Stack()
# for n in l:
#     s.push(n)
#
# s.pop()
# s.push('a')
# s.push('b')
# s.pop()
#
# while not s.is_empty():
#     print(s.pop(), end='>')
# print()
# # ans is a > 3 > 1
