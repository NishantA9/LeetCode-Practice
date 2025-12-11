from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # sort by start then end
        res = 0  # count of intervals to remove
        prevEnd = intervals[0][1]  # end of last kept interval
        for start, end in intervals[1:]:  # iterate remaining intervals
            if start >= prevEnd:  # no overlap
                prevEnd = end  # keep this interval
            else:
                res += 1  # overlap -> need to remove one
                prevEnd = min(end, prevEnd)  # keep interval with smaller end to reduce future overlaps
        return res  # minimum removals