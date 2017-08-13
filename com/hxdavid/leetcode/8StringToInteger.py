class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None or len(str) == 0:
            return 0
        res, min_int, max_int = 0, -(1 << 31), (1 << 31) - 1
        str = str.strip()
        is_negative = len(str) > 0 and str[0] == '-'
        str = str[1:] if len(str) > 0 and str[0] in '+-' else str
        for ch in str:
            if ch < '0' or ch > '9':
                return res
            elem = -int(ch) if is_negative else int(ch)
            res = res * 10 + elem
            if res > max_int:
                return max_int
            elif res < min_int:
                return min_int
        return res


print(Solution().myAtoi("  -0012a42"))
