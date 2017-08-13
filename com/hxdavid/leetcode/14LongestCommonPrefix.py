class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0 or len(strs[0]) == 0:
            return res
        for i, ch in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or ch != strs[j][i]:
                    return res
            res += ch
        return res
