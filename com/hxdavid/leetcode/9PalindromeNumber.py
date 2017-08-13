class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        p, q = x, 0
        while p > 0:
            q = q * 10 + p % 10
            p //= 10
        return q == x

    def isPalindrome2(self, x):
        """
        An Optimised Version of isPalindrome function

        :type x: int
        :rtype: bool
        """
        # Optimizations
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        if x < 100 and x % 11 == 0:
            return True
        if x < 1000 and ((x // 100) * 10 + x % 10) % 11 == 0:
            return True

        # Actual logic
        v = x % 10
        x //= 10
        while x - v > 0:
            v = v * 10 + x % 10
            x //= 10
        if v > x:
            v //= 10
        return v == x


print(Solution().isPalindrome(98765432100123456789))
