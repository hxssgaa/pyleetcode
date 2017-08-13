class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum, temp = nums[0], 0
        for num in nums:
            temp = max(num, temp + num)  # Some "If" condition can be replaced by max or min.
            max_sum = max(temp, max_sum)
        return max_sum
