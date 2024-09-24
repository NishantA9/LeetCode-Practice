from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers:
        # 'l' is the left pointer, starting from the beginning of the list
        # 'r' is the right pointer, starting from the end of the list
        l, r = 0, len(numbers) - 1  # noqa: E741
        
        # Continue the loop until the two pointers meet
        while l < r:
            # Calculate the current sum of the two numbers at the left and right pointers
            curSum = numbers[l] + numbers[r]
            
            # If the current sum is greater than the target, move the right pointer to the left
            # This is because the list is sorted, and reducing 'r' will decrease the sum.
            if curSum > target:
                r -= 1
            
            # If the current sum is less than the target, move the left pointer to the right
            # Moving 'l' to the right increases the sum because the list is sorted.
            elif curSum < target:
                l += 1  # noqa: E741
            
            # If the current sum equals the target, return the 1-based indices of the two numbers
            else:
                return [l + 1, r + 1]  # Add 1 to both 'l' and 'r' to convert 0-based to 1-based indexing
        
        # If no solution is found (though the problem guarantees one solution), return an empty list
        return []
