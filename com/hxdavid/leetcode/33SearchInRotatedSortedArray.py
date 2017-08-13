class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n, low, high = len(nums), 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
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
        return low if nums[low] == target else -1


print(Solution().search([4, 3, 2, 1, 0], 1))
