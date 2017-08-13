class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res, min_int, max_int = 0, -(1 << 31), (1 << 31) - 1
        if x < 0:
            r = -self.reverse(-x)
            return 0 if r < min_int else r
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
        return 0 if res > max_int else res


print(Solution().reverse(1234567890))
