class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [x for x in nums if x != val]  # This would set the content of the nums.
        return len(nums)


lst = [3, 2, 2, 3]
print(Solution().removeElement(lst, 3))
print(lst)
