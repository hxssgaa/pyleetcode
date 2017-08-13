class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return float(x) * self.myPow(x, n - 1)  # Use float to avoid massive integer calculation.
        return self.myPow(float(x) * x, n / 2)


print(Solution().myPow(2, -1231231222))
