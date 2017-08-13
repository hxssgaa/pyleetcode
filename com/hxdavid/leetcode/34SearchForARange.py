class Solution(object):
    def search(self, nums, target, up_bound=False):
        low, high, bound = 0, len(nums) - 1, int(up_bound)
        while low < high:
            mid = (low + high + bound) // 2
            if nums[mid] >= target + bound:
                high = mid - bound
            else:
                low = mid + 1 - bound
        return low if nums[low] == target else -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.search(nums, target, False),
                self.search(nums, target, True)]


print(Solution().searchRange([2, 2], 1))