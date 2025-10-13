from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Add original index to each task for tracking
        for i, t in enumerate(tasks):
            t.append(i)  # [enqueueTime, processingTime, originalIndex]
        tasks.sort(key=lambda t: t[0])        # Sort tasks by enqueue time
        res, minHeap = [], []  # Result list and min heap for available tasks
        i, time = 0, tasks[0][0]  # Task index and current time
        while minHeap or i < len(tasks):        # Process all tasks
            while i < len(tasks) and time >= tasks[i][0]:  # Add all tasks that are available at current time to heap
                # Push [processingTime, originalIndex] to prioritize by processing time
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1            
            if not minHeap:  # No tasks available, jump to next task's enqueue time
                time = tasks[i][0]
            else:
                # Process the task with shortest processing time (and lowest index if tie)
                procTime, index = heapq.heappop(minHeap)
                time += procTime  # Update current time
                res.append(index)  # Add original index to result
        return res