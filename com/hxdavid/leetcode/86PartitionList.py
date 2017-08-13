# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node1, node2 = ListNode(0), ListNode(0)
        p1, p2 = node1, node2
        while head:
            if head.val < x:
                p1.next = p1 = head  # Python assigns variables from left to right to the value.
            else:
                p2.next = p2 = head
            head = head.next
        p1.next, p2.next = node2.next, None
        return node1.next


def printNode(head):
    while head:
        print(head.val, end=" ")
        head = head.next


printNode(Solution().partition(ListNode(5, ListNode(4, ListNode(3, ListNode(2)))), 3))
