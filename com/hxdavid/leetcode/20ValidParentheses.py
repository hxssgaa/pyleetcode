class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for e in s:
            if e == '(' or e == '[' or e == '{':
                stk.append(e)
            elif e == ')' and stk and stk[-1] == '(':
                stk.pop()
            elif e == ']' and stk and stk[-1] == '[':
                stk.pop()
            elif e == '}' and stk and stk[-1] == '{':
                stk.pop()
            else:
                return False
        return not stk


print(Solution().isValid("([])"))
