class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        g = [0] * (n + 1)
        g[0] = g[1] = 1

        for i in xrange(2, n + 1):
            for j in xrange(1, i + 1):
                g[i] += g[j - 1] * g[i - j]

        return g[n]


print Solution().numTrees(2000)