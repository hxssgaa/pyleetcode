import time


class Solution(object):
    def generateParenthesisHelper(self, cur, left, right, n, result):
        """
        :type cur: str
        :type left: int
        :type right: int
        :type n: int
        :type result: list
        """
        if left == n and left == right:
            result.append(cur)
            return
        if left == right:
            cur += "("
            self.generateParenthesisHelper(cur, left + 1, right, n, result)
            return
        if left == n:
            cur += ")"
            self.generateParenthesisHelper(cur, left, right + 1, n, result)
            return
        self.generateParenthesisHelper(cur + "(", left + 1, right, n, result)
        self.generateParenthesisHelper(cur + ")", left, right + 1, n, result)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generateParenthesisHelper("", 0, 0, n, res)
        return res


s = time.clock()
res = Solution().generateParenthesis(13)
e = time.clock()
print("\n".join(res))
print("costs time:" + str(e - s) + "s")
