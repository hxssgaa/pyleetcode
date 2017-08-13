# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        This algorithm use "two-pointer" technique to solve this problem.
        Note that the usage of dummy node in linked list is usually useful.

        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next if head is not None else None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
        if slow.next != None:
            slow.next = slow.next.next
        return head


h = ListNode(1)
h.next = ListNode(2)
res = Solution().removeNthFromEnd(h, 1)
print(res)
