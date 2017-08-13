class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, longest = len(s), 0
        st = []
        for i in range(n):
            if s[i] != '(' and st and s[st[-1]] == '(':
                st.pop()
            else:
                st.append(i)
        if not st:
            longest = n
        else:
            b = n - 1
            while st:
                top = st[-1]
                longest = max(b - top, longest)
                b = top - 1
                st.pop()
            longest = max(b + 1, longest)
        return longest


print(Solution().longestValidParentheses("()"))
print(Solution().longestValidParentheses("((((()))()()()()()()()()))()()()()()()()()))))))(((((()()()))"))
