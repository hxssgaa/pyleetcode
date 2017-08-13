# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self, *args, **kwargs):
        h = self
        res = ""
        while h:
            res += str(h.val) + "->"
            h = h.next
        return res[:-2]


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            """
            Use tail to keep track of new linked list using the original space in l1 and l2.
            After one list finished merging, we only need to set next node of the tail to the head of remaining
            not empty list.
            """
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next

    def mergeKLists(self, lists):
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        while len(lists) > 1:
            lists.append(self.mergeTwoLists(lists[0], lists[1]))
            del lists[:2]
        return lists[0]


print(ListNode(None))
