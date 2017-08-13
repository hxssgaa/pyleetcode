from functools import reduce


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return reduce(lambda P, e: [p[:i] + [e] + p[i:] for p in P for i in range((p + [e]).index(e) + 1)], nums, [[]])
