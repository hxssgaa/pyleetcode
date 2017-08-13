class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):  # We can't use enumerate nums because the nums[i] is always changing.
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                """
                It is crucial to remember in python swap can be dangerous, the following statement can only be
                used without changing the value of nums[i], because it's interpreted left to right,
                it could cause misuse.
                """
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return n + 1


print(Solution().firstMissingPositive([3, 4, -1, 1]))
