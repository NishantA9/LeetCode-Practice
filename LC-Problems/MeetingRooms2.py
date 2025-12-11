"""Definition of Interval: """
from typing import List
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])  # sorted list of start times
        end = sorted([i.end for i in intervals])  # sorted list of end times
        res = count = 0  # res: max rooms needed, count: current rooms in use
        s = e = 0  # pointers for start and end lists
        while s < len(intervals):  # process each meeting start
            if start[s] < end[e]:  # next meeting starts before earliest end -> need a new room
                s += 1
                count += 1
            else:
                e += 1  # one meeting ended -> free a room
                count -= 1
            res = max(res, count)  # track maximum concurrent rooms
        return res