import time


class Solution(object):
    def combine_slow(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        Remember the following statement is basically cartesian product of [1:n+1] X combine(i-1,k-1)
        But avoid cartesian product, because of the performance issue.
        """
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n + 1) for pre in self.combine_slow(i - 1, k - 1)]

    def dfs(self, n, k, s, temp, res):
        if k <= 0:
            res.append(temp)
            return
        for i in range(s, n - k + 1):  # Pruning, it won't exceed n - k + 1
            self.dfs(n, k - 1, i + 1, temp + [i + 1], res)

    def combine(self, n, k):
        res = []
        self.dfs(n, k, 0, [], res)
        return res


n, k = 10, 5
s = time.clock()
print(Solution().combine(n, k))
e = time.clock()
print(e - s)
a1 = ["a", "b", "c"]
a2 = ["d", "e", "f"]
res = [(x, y) for x in a1 for y in a2 + [x]]
print(res)
