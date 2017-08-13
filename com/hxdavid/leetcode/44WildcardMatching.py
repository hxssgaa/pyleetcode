class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False
        ns, np = len(s), len(p)
        dp = [[False for j in range(np + 1)] for i in range(ns + 1)]
        dp[0][0] = True
        for j in range(1, np + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '?')
        return dp[ns][np]
