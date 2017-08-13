class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = [0] * (len(nums1) + len(nums2))
        cur1, cur2, cnt = 0, 0, 0
        while cur1 < len(nums1) or cur2 < len(nums2):
            if cur1 == len(nums1):
                res[cnt] = nums2[cur2]
                cnt += 1
                cur2 += 1
                continue
            if cur2 == len(nums2):
                res[cnt] = nums1[cur1]
                cnt += 1
                cur1 += 1
                continue
            if nums1[cur1] < nums2[cur2]:
                res[cnt] = nums1[cur1]
                cnt += 1
                cur1 += 1
            else:
                res[cnt] = nums2[cur2]
                cnt += 1
                cur2 += 1
        if len(res) % 2 != 0:
            return res[len(res) // 2]
        else:
            return (res[(len(res) - 1) // 2] + res[len(res) // 2]) / 2.0


print(Solution().findMedianSortedArrays([1, 2], [3, 4, 5, 6, 7]))
arr = [1, 2, 3, 4, 5, 6]