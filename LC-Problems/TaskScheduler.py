from collections import Counter, deque 
import heapq
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)  # Step 1: Count frequencies of each task
        maxHeap = [-cnt for cnt in count.values()] # Step 2: Use a max heap (negate values because Python has min heap by default)
        heapq.heapify(maxHeap)
        time = 0  # Total time counter
        q = deque()  # Queue to manage cooldown => [remaining_count, ready_time]
        while maxHeap or q: # Step 3: Process until all tasks are done
            time += 1
            if maxHeap: # Step 4: If heap has tasks, pop the one with highest remaining count
                cnt = 1 + heapq.heappop(maxHeap)  # Do one unit of work (so +1 towards 0)
                if cnt:  # If still remaining, put in cooldown queue
                    q.append([cnt, time + n])
            if q and q[0][1] == time:  # Step 5: If front of queue is ready to re-enter heap, push it back
                heapq.heappush(maxHeap, q.popleft()[0])
        return time  # Total time taken including idle slots if any