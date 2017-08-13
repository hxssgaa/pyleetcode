# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_node(head):
    """
    :type head: ListNode
    """
    while head:
        print(head.val, end=" " if head.next else "")
        head = head.next
    print()
