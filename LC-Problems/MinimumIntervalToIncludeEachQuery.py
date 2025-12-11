from typing import List
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()  # sort intervals by start
        minHeap = []  # heap of (size, right) for intervals that started before or at query
        res = {}  # store answer per query value
        i = 0  # pointer into intervals
        for q in sorted(queries):  # process queries in increasing order
            while i < len(intervals) and intervals[i][0] <= q:  # add all intervals whose start <= q
                l, r = intervals[i]  # noqa: E741
                heapq.heappush(minHeap, (r - l + 1, r))  # push (size, right)
                i += 1
            while minHeap and minHeap[0][1] < q: # remove intervals that end before q (not covering q)
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1  # top of heap is smallest size covering q (if any)
        return [res[q] for q in queries]  # map back to original query order