# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype: list[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        result = []
        start, end = intervals[0].start, intervals[0].end
        for interval in intervals:
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                result.append(Interval(start, end))
                start = interval.start
                end = interval.end
        result.append(Interval(start, end))
        return result


for e in Solution().merge([Interval(2, 6), Interval(1, 3), Interval(8, 10), Interval(15, 18)]):
    print("%s,%s" % (e.start, e.end))
