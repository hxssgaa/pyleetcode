class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, elem in enumerate(nums):
            if target - elem not in num_map:
                num_map[elem] = i
            else:
                return [num_map[target - elem], i]
        return [-1, -1]


print(Solution().twoSum([9, 5, 1, 2, 92, 234, 232, 2342342, 342, 2395, 4234], 4236))
