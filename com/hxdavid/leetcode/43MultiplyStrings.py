from time import clock


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return "0"
        n1, n2, n = len(num1), len(num2), 1
        if n1 < n2:
            return self.multiply(num2, num1)
        num1, num2 = num1[::-1], num2[::-1]
        ans = bytearray("0" * (n1 + n2), "UTF-8")  # Use byte array to create mutable strings, the element type is int
        i, j = 0, 0
        for i in range(n1):
            up = 0
            e1 = int(num1[i])
            for j in range(n2):
                e2 = int(num2[j])
                res = e1 * e2 + up + ans[i + j] - ord('0')
                ans[i + j] = res % 10 + ord('0')
                if i + j + 1 > n and ans[i + j] != ord('0'):
                    n = i + j + 1
                up = res // 10
            j += 1
            if up > 0:
                ans[i + j] = up + ord('0')
                if i + j + 1 > n:
                    n = i + j + 1
        ans = ans[:n][::-1]
        return "0" if n == 0 else ans.decode("UTF-8")


str1 = ""
str2 = ""
for i in range(100):
    str1 += str(i)
    str2 += str(i * 2)
start = clock()
print(Solution().multiply(str1, str2))
end = clock()
print("time costs:" + str(end - start))
