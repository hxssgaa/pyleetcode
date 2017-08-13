import bisect
from time import clock


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)


lst = []
for i in range(10000000):
    lst.append(i * 2)
start = clock()
res = Solution().searchInsert(lst, 1234)
end = clock()
print("costs:" + str(end - start))
print("res:" + str(res))
