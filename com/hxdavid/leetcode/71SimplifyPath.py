class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        for p in [p for p in path.split("/") if p != "." and p]:
            if p == ".." and stk:
                stk.pop()
            elif p != "..":
                stk.append(p)
        return "/" + "/".join(stk)


print(Solution().simplifyPath("/abc/./def/cfg/../../../../"))
