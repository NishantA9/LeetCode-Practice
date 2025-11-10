from typing import List
"""Definition of Interval: """
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)  # sort meetings by start time
        for i in range(1, len(intervals)):  # check each adjacent pair for overlap
            i1 = intervals[i - 1]  # previous interval
            i2 = intervals[i]  # current interval
            if i1.end > i2.start:  # overlap detected
                return False  # cannot attend all meetings
        return True  # no overlaps found, can attend all meetings