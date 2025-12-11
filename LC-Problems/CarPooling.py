from typing import List
import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])  # Sort trips by start time
        minHeap = []  # Min heap to store [end_time, num_passengers]
        curPass = 0   # Current number of passengers in the car
        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:  # Remove passengers whose trips have ended before current start time
                curPass -= heapq.heappop(minHeap)[1]  # Subtract passengers getting off        
            curPass += numPass  # Add new passengers getting on            
            if curPass > capacity:# Check if current passenger count exceeds capacity
                return False           
            heapq.heappush(minHeap, [end, numPass]) # Add current trip's end time and passenger count to heap    
        return True  # All trips can be completed within capacity