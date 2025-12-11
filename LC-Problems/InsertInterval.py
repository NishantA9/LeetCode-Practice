from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []  # result list to collect non-overlapping intervals
        for i in range(len(intervals)):
            # If new interval comes before the current interval and no overlap
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)  # place newInterval before current
                return res + intervals[i:]  # append the rest and return
            # If new interval comes after the current interval and no overlap
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])  # keep current interval
            else:
                # Overlapping intervals -> merge into newInterval
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # new start
                    max(newInterval[1], intervals[i][1]),  # new end
                ]
        res.append(newInterval)  # if newInterval not placed yet, append at end
        return res  # final merged list