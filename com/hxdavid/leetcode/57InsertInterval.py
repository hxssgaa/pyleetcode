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

    """
    The first insert interval algorithm is based on the merge algorithm implemented in 56th problem.
    Basically the algorithm is to merge the intervals after inserting new interval.

    This algorithm is better since it handles overlapping intervals as well.
    """
    def insert(self, intervals, newInterval):
        """
        :type intervals: list[Interval]
        :type newInterval: Interval
        :rtype: list[Interval]
        """
        if not intervals:
            return [newInterval]
        return self.merge(intervals + [newInterval])

    """
    The second insert interval algorithm first init the start, end to be the new interval's start and end.
    After finding start less than intervals[i].end, we can keep enlarging the start, end until the end is less than
    interval[i].start. Then we can just break the loop and append the rest result.

    However the first algorithm is better because it handles overlapping intervals.
    """
    def insert2(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1
        result.append(Interval(start, end))
        result += intervals[i:]
        return result


for e in Solution().insert([Interval(3, 100), Interval(101, 200), Interval(20, 300), Interval(600, 700), Interval(800, 900)],
                           Interval(700, 800)):
    print("%s,%s" % (e.start, e.end))
