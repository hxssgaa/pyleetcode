# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        The algorithm basically use cur node to keep track of the most left node.
        And use stack to store all the left nodes, so we can keep appending
        all the left node of the cur, and pop one out, append it to the result
        and move to the right.
        """
        stk, result = [], []
        cur = root
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            result.append(cur.val)
            cur = cur.right
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    print Solution().inorderTraversal(root)
