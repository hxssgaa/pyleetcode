class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n, low, high = len(nums), 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[high]:
                if nums[mid] > target >= nums[low]:
                    high = mid
                else:
                    low = mid + 1
            elif nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid
            else:
                high -= 1
        return nums[low] == target


print(Solution().search([1, 1], 1))
