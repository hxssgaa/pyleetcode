class Solution(object):
    def climbStairs(self, n):
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


print(Solution().climbStairs(1928391823918293819))
