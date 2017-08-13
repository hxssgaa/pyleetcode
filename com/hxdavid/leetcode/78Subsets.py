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
            self.dfs(nums, path + [nums[i]], res, i + 1)

    def subsets(self, nums):
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        res = []
        self.dfs(nums, [], res, 0)
        return res


for l in Solution().subsets([1, 2, 3]):
    print(l)
