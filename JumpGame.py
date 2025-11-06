from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # 'goal' is the index we want to reach, initially the last index
        for i in range(len(nums) - 1, -1, -1): # Traverse the array backwards from the second-to-last element to the first
            if i + nums[i] >= goal: # If from the current position i, we can jump to or beyond the 'goal'
                goal = i  # Move the goal to the current index 'i'        
        return True if goal == 0 else False # After the loop, check if we have moved the goal to the start (index 0)