from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])  # sort by start time
        output = [intervals[0]]  # initialize output with first interval
        for start, end in intervals:  # iterate through intervals
            lastEnd = output[-1][1]  # end of last interval in output
            if start <= lastEnd:  # overlap -> merge
                output[-1][1] = max(lastEnd, end)  # extend the end if needed
            else:
                output.append([start, end])  # no overlap -> add new interval
        return output  # merged intervals