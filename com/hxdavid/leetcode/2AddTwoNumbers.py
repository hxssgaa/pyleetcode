# Definition for singly-linked list.
import time


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry /= 10
        return dummy.next


head1 = ListNode(1)
cur1 = head1
head2 = ListNode(2)
cur2 = head2
for i in range(1000000):
    cur1.next = ListNode(i % 10)
    cur2.next = ListNode(i % 10)
    cur1 = cur1.next
    cur2 = cur2.next
start = time.clock()
res = Solution().addTwoNumbers(head1, head2)
end = time.clock()
print("read: %f s" % (end - start))
print(res.val)
