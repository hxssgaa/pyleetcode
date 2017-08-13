from com.hxdavid.utility.utility import *


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        s = 1
        while head and s < m:
            head = head.next
            pre = pre.next
            s += 1
        while head and s < n:
            before = pre.next
            cur = head.next
            head.next = head.next.next
            pre.next = cur
            cur.next = before
            s += 1
        return dummy.next


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
print_node(Solution().reverseBetween(h, 2, 3))
