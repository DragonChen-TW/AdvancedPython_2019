# Important
# 非常抱歉我上次說的這個做法非常不好
# 因為每次執行 push pop 都需要 O(n) 的複雜度
# 所以這是很不好的作法
# 很抱歉我上禮拜準備教材太匆忙
# 完全沒有發現這根本不是好的做法
# 正確的、簡短的作法已經更新在 hw1_ans

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

# Let's do a linked-list version stack
# Functions: push, pop, is_empty
class Stack:
    def __init__(self):
        self.head = None

    def push(self, n):
        if not self.head: # if head is None
            self.head = Node(n)
        else:              # have node(s)
            now = self.head     # reference to head, like a c pointer
            while now.next:     # iter to the last one
                now = now.next
            now.next = Node(n)

    def pop(self):
        if self.head is None:
            pass
        elif not self.head.next:  # just one node is list
            temp = self.head
            self.head = None
        else:   # more than one
            now = self.head
            while now.next.next:     # iter to the last one
                now = now.next
            temp = now.next
            now.next = None

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

print_linked_list(s.head)
# expect '1 > 3 > a >'
# but its not the stack's pop order

while not s.is_empty():
    print('{} > '.format(s.pop()),end='')
print()
# ans is 'a > 3 > 1 >'
# it is
