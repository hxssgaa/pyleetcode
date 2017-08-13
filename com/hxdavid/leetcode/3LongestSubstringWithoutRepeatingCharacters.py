class Solution(object):
    def lengthOfLongestSubstring(self, st):
        """
        :type st: str
        :rtype: int
        """
        if len(st) == 0:
            return 0
        hashy = {}
        i, j, mx = 0, 0, 0
        for k, v in enumerate(st):
            if v in hashy:
                j = j if j > hashy[v] + 1 else hashy[v] + 1
            hashy[v] = k
            mx = mx if mx > i - j + 1 else i - j + 1
            i += 1
        return mx


print(Solution().lengthOfLongestSubstring("pwwaaaakewffghyqw6"))
