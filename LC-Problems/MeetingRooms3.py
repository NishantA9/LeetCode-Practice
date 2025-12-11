import heapq
from typing import List
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # sort meetings by start time
        available = [i for i in range(n)]  # min-heap of available room ids
        used = []  # min-heap of busy rooms as (end_time, room_id)
        count = [0] * n  # number of meetings assigned to each room
        for start, end in meetings:
            while used and used[0][0] <= start: # free up rooms that finished by 'start'
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            if not available:
                end_time, room = heapq.heappop(used) # no free room: wait for the earliest to be free
                end = end_time + (end - start)  # schedule this meeting after that end
                heapq.heappush(available, room)
            room = heapq.heappop(available)  # pick smallest-numbered available room
            heapq.heappush(used, (end, room))  # mark room busy until 'end'
            count[room] += 1  # increment meeting count for this room
        return count.index(max(count))  # return room with most meetings (ties -> smallest idx)