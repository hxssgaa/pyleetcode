import random


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 1:
            return 0
        elif x == 1:
            return 1
        low, high = 1, x // 2
        while low < high:
            mid = low + (high - low + 1) // 2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                low = mid
            else:
                high = mid - 1

    # This is perhaps fastest code to solve int sqrt.
    def mySqrt2(self, x):
        if x == 0:
            return 0
        h = 0
        while (1 << h) * (1 << h) <= x:
            h += 1
        h -= 1
        b = h - 1
        res = 1 << h
        while b >= 0:
            if (res | (1 << b)) * (res | (1 << b)) <= x:
                res |= (1 << b)
            b -= 1
        return res


str = "".join(str(i % 10) for i in range(10000))
print(str)
print(Solution().mySqrt2(int(str)))
