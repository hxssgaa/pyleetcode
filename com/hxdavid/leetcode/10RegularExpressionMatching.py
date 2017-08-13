class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        """
        This is the correct way to define matrix, do not use ([False] * (m + 1)) * (n + 1), this would copy the
        reference of objects.
        """
        dp = [[False for x in range(m + 1)] for y in range(n + 1)]
        """
        If p and s is both empty, we got a match.
        """
        dp[0][0] = True
        """
        If p is empty, while s is not empty, dp is 0.
        However, if s is empty, while p is not empty, we should calculate the dp.
        j > 1 means * and empty string return false.
        """
        for j in range(1, m + 1):
            dp[0][j] = p[j - 1] == '*' and j > 1 and dp[0][j - 2]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or ((s[i - 1] == p[j - 2] or '.' == p[j - 2]) and dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or '.' == p[j - 1])
        return dp[n][m]


print(Solution().isMatch("abcdef", "*bcd*"))
