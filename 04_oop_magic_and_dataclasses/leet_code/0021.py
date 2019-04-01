# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        save = new_l = None
        if l1 and l2:
            if l1.val <= l2.val:
                save = new_l = ListNode(l1.val)
                l1 = l1.next
            else:
                save = new_l = ListNode(l2.val)
                l2 = l2.next

            while l1 and l2:
                if l1.val <= l2.val:
                    new_l.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    new_l.next = ListNode(l2.val)
                    l2 = l2.next

                new_l = new_l.next

        if l1:
            if new_l:
                new_l.next = l1
            else:
                save = l1
        if l2:
            listPrint(new_l)
            listPrint(l2)
            if new_l:
                new_l.next = l2
            else:
                save = l2

        return save


def listPrint(l):
    while l:
        print(l.val, '->', end=' ')
        l = l.next
    print('null')

def makeList(nums):
    head = now = ListNode(nums[0])
    for i in range(1, len(nums)):
        now.next = ListNode(nums[i])
        now = now.next
    return head

if __name__ == '__main__':
    l1 = makeList([1, 2, 4])
    l2 = makeList([1, 3, 4])
    s = Solution()

    # listPrint(l1)
    # listPrint(l2)
    listPrint(s.mergeTwoLists(l1, l2))
