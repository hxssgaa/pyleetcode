from functools import reduce

import math


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = n + m - 2  # How much steps we need to do
        k = m - 1  # Number of steps that need to go down
        """
        Here we calculate the total possible path number
        Combination(l, k) = n! / (k!(n - k)!)
        Reduce the numerator and denominator and get
        C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!

        Remember that the division is different between Python 2 and Python 3.
        """
        return reduce(lambda x, y: x * y, ((l - k + i) for i in range(1, k + 1)), 1) / math.factorial(k)


print(Solution().uniquePaths(10, 10))
