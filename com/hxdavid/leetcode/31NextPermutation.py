class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        i, j = n - 2, n - 1
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        while i != -1 and i < j - 1 and nums[j] <= nums[i]:
            j -= 1
        if i != -1:
            nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


lst = [1, 2, 3, 4, 5, 6, 7]
Solution().nextPermutation(lst)
print(lst)
