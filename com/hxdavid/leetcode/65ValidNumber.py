class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True


print(Solution().isNumber("0"))
print(Solution().isNumber(" 0.1 "))
print(Solution().isNumber("abc"))
print(Solution().isNumber("1 a"))
print(Solution().isNumber("2e10"))
