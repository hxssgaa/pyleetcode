class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        while n > 0 and s[n - 1] == ' ':
            n -= 1
        i = n
        while i > 0 and s[i - 1] != ' ':
            i -= 1
        return n - i

print(Solution().lengthOfLastWord("a"))