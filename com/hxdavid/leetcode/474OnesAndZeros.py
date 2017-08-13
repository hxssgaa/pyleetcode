class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: list[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # Use dp to solve this problem.
        dp = [([0] * (n + 1)) for _ in range(m + 1)]
        # We can keep updating the dp for each element in strs to get the final answer.
        for s in strs:
            # Get how many zero and ones in the str.
            t = (s.count("0"), s.count("1"))
            """
            The reason we calculate the dp backwards is that we MUST use PREVIOUSLY dp.
            And dp[i][j] = max(1 - dp[i - t[0]][j - t[1]], dp[i][j], remember that the
            the dp[i][j] remains the same if i - t[0] < 0 or j - t[1] < 0, and we must not
            calculate the dp with asc iterating order. Because it would interfere the outcome
            of the dp[i][j].
            """
            for i in range(m, t[0] - 1, -1):
                for j in range(n, t[1] - 1, -1):
                    dp[i][j] = max(1 + dp[i - t[0]][j - t[1]], dp[i][j])
        return dp[m][n]


print(Solution().findMaxForm(["111", "1000", "1000", "1000"], 9, 3))
