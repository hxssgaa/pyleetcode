import collections

from functools import reduce


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: list[str]
        :rtype: list[list[str]]
        """
        m = collections.defaultdict(list)
        for s in strs:
            m["".join(sorted(s))].append(s)
        return [p for p in m.values()]


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
