import random


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(remain, stk):
            if remain == 0:  # Use remain to keep track of remaining diff to the target.
                res.append(stk)
                return

            for item in candidates:
                if item > remain:  # Get rid of element which is greater than remain
                    break
                if stk and item < stk[-1]:  # Get rid of element which is smaller than the top element of the stack
                    continue
                else:
                    dfs(remain - item, stk + [item])

        dfs(target, [])
        return res


lst = []
for i in range(1000):
    lst.append(int(random.random() * 10000))
print(Solution().combinationSum(lst, 5555))
