class Solution(object):
    def dfs(self, nums, path, res, s):
        """
        :type nums: list[int]
        :type path: list[int]
        :type res: list[list[int]]
        :type s: int

        This algorithm use s to indicate the start position of the nums.
        So we can get different paths which ranges from (s:len(nums))
        """
        res.append(path)
        for i in range(s, len(nums)):
            if i > s and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, path + [nums[i]], res, i + 1)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), [], res, 0)
        return res
