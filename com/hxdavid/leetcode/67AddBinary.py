class Solution(object):
    def addBinary(self, a, b):
        """
        This example demonstrates how to convert integer to binary
        and vice versa.
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


print(Solution().addBinary("100", "001"))
