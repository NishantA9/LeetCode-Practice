from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0  # 'res' keeps track of the number of jumps
        l = r = 0  # 'l' is the left boundary, 'r' is the right boundary of the current window of positions we can jump from  # noqa: E741
        while r < len(nums) - 1: # Continue until we reach or go beyond the last index
            farthest = 0  # 'farthest' keeps track of the farthest position we can jump to in the current window
            for i in range(l, r + 1):  # Iterate over the current window of positions (from l to r)
                farthest = max(farthest, i + nums[i]) # Update the farthest position we can jump to
            l = r + 1  # Move the window to the right: the new left boundary is 'r + 1' # noqa: E741
            r = farthest # Update the right boundary to 'farthest'
            res += 1  # Increment the number of jumps
        return res  # Return the total number of jumps