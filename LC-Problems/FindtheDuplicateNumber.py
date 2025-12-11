from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize two pointers (slow and fast)
        slow, fast = 0, 0
        # Step 2: Use Floyd's Cycle Detection to detect cycle
        while True:
            slow = nums[slow]  # Move slow pointer one step
            fast = nums[nums[fast]]  # Move fast pointer two steps
            if slow == fast:  # Cycle detected
                break
        # Step 3: Find entry point of the cycle (duplicate number)
        slow2 = 0
        while True:
            slow = nums[slow]  # Move slow one step
            slow2 = nums[slow2]  # Move slow2 one step
            if slow == slow2:  # When they meet, it's the duplicate
                return slow