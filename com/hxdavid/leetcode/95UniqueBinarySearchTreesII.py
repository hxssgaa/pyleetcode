from __future__ import print_function


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTreesHelper(self, n, less_than, greater_than):
        """
        :type n: int
        :type less_than: int
        :type greater_than: int
        :rtype: List[Tuple[TreeNode, int]]
        """
        rst = []
        for i in xrange(1 if greater_than == - 1 else greater_than + 1,
                        n + 1 if less_than == -1 else less_than):  # Suppose first node value is i.
            left_list = self.generateTreesHelper(n, i, greater_than)
            right_list = self.generateTreesHelper(n, less_than, i)
            if not right_list:
                for l_tree in left_list:
                    new_node = TreeNode(i)
                    new_node.left = l_tree
                    rst.append(new_node)
            if not left_list:
                for r_tree in right_list:
                    new_node = TreeNode(i)
                    new_node.right = r_tree
                    rst.append(new_node)
            if left_list and right_list:
                for l_tree in left_list:
                    for r_tree in right_list:
                        new_node = TreeNode(i)
                        new_node.left = l_tree
                        new_node.right = r_tree
                        rst.append(new_node)
            if not left_list and not right_list:
                new_node = TreeNode(i)
                rst.append(new_node)

        return rst

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateTreesHelper(n, -1, -1)


def pre_order(root):
    if not root:
        return
    print(root.val, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val, end=' ')
    in_order(root.right)


def _main():
    roots = Solution().generateTrees(10)
    for r in roots:
        pre_order(r)
        print("    ", end=' ')
        in_order(r)
        print()


if __name__ == '__main__':
    _main()
