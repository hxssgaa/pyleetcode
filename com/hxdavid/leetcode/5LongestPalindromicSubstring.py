class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, n, max_len, start = 0, len(s), 1, 0
        if s is None or n == 0 or n == 1:
            return s
        while i < n:
            if n - i <= max_len // 2:
                break
            j = k = i
            while k < n - 1 and s[k] == s[k + 1]:
                k += 1
            i = k + 1
            while k < n - 1 and j > 0 and s[k + 1] == s[j - 1]:
                k += 1
                j -= 1
            if k - j + 1 > max_len:
                start = j
                max_len = k - j + 1
        return s[start:start + max_len]


print(Solution().longestPalindrome("jhgghjklasdkjwjrqioruqowiuorqijksajdkasjdkasjdkasjda"
                                   "kjhqwertyuytrewqajshdjahsjdhafsdkfjsdkfjsdjfksjdkfjsdkjfksdjfksdqoiroripwq"
                                   "jsdfklsdkfl2eisdvnsjdkfjksjfkasjfkaspqwoirqwiroqiworiqowiroqwiroqwiroqwpfjkjfkaj"
                                   "aasdadksajdkajdkajskdjaskdjaskdjakjdkasjdkndvasdasdasvoevwhvhwehviwehvwhvwie"
                                   "asdasdjkajsdqlkjhgfdsaasdfghjklqkasjdqpwjdoqwjdoqjwojwqodqow"))
