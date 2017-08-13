import itertools
from functools import reduce


class Solution(object):
    def permute(self, nums):
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        # It's recommended to use "or" default value statement and generator to get arrays.
        return [[e] + p for i, e in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]

    def permute2(self, nums):
        # Remember reduce can get any type of result(not just reduce) based on how you organise it.
        # It's kind of hard to get to know how reduce works, remember the first element is the same type as result
        # Which means P = func(P, e), so P is the iterate result.
        # So you cam think of this function by appending new e number to each old list P in every position.
        return reduce(lambda P, e: [p[:i] + [e] + p[i:] for p in P for i in range(len(p) + 1)], nums, [[]])

    def permute3(self, nums):
        return list(itertools.permutations(nums))


for l in Solution().permute2([1, 2, 3]):
    print(l)


def myreduce(fnc, seq, init):
    tally = init
    for next in seq:
        tally = fnc(tally, next)
    return tally


print(myreduce(lambda x, y: [l[:i] + [y] + l[i:] for l in x for i in range(len(l) + 1)], [1, 2, 3, 4], [[]]))
