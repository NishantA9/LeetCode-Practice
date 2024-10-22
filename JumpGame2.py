from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0  # 'res' keeps track of the number of jumps
        l = r = 0  # 'l' is the left boundary, 'r' is the right boundary of the current window of positions we can jump from  # noqa: E741

        # Continue until we reach or go beyond the last index
        while r < len(nums) - 1:
            # 'farthest' keeps track of the farthest position we can jump to in the current window
            farthest = 0

            # Iterate over the current window of positions (from l to r)
            for i in range(l, r + 1):
                # Update the farthest position we can jump to
                farthest = max(farthest, i + nums[i])

            # Move the window to the right: the new left boundary is 'r + 1'
            l = r + 1  # noqa: E741
            # Update the right boundary to 'farthest'
            r = farthest
            # Increment the number of jumps
            res += 1

        # Return the total number of jumps
        return res
