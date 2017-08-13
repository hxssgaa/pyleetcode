class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        For each bit position 1-32 in a 32-bit integer, we count the number of integers in the array which have
        that bit set. Then, if there are n integers in the array and k of them have a particular bit set and
        (n-k) do not, then that bit contributes k*(n-k) hamming distance to the total.
        """
        total, n = 0, len(nums)
        for j in range(0, 32):
            bit_count = sum((nums[i] >> j) & 1 for i in range(0, n))
            total += bit_count * (n - bit_count)
        return total


print(Solution().totalHammingDistance([4, 14, 2]))
