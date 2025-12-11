from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:        # Step 1: Check if total sum is odd
            return False  # Odd sums can't be split evenly
        dp = set()
        dp.add(0)  # Base case: subset sum of 0 is always possible
        target = sum(nums) // 2
        for i in range(len(nums) - 1, -1, -1):        # Step 2: Iterate through nums from back
            nextDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True  # Found a subset that adds up to target
                nextDp.add(t + nums[i])  # Include current number
                nextDp.add(t)            # Exclude current number
            dp = nextDp  # Move to next state
        return True if target in dp else False