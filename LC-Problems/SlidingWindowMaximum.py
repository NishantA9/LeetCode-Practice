from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []  # Stores the maximum of each window
        q = deque()  # Deque to store indices of elements in decreasing order
        l, r = 0, 0  # Left and right pointers for the sliding window  # noqa: E741

        while r < len(nums):  # Iterate through the list
            while q and nums[q[-1]] < nums[r]: # Remove elements from the back of deque if they are smaller than nums[r]
                q.pop()  # Pop from back as they are not useful
            q.append(r)  # Add the current element index to the deque
            
            if l > q[0]: # Remove the leftmost element from the deque if it's outside the window
                q.popleft()  # Pop from front
            if (r + 1) >= k: # When the window reaches size k, start recording the max values
                output.append(nums[q[0]])  # Front of deque is the max of the window
                l += 1  # Move the left pointer to slide the window  # noqa: E741
            r += 1  # Expand the window by moving the right pointer
        return output  # Return the list of maximum values for each window