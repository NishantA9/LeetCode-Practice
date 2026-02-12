'''
Suppose nums = [1, 2, 3, 4, 5, 6, 7] and k = 3:
After calculating k = k % len(nums), k remains 3.
Reverse the entire array: [7, 6, 5, 4, 3, 2, 1].
Reverse the first k elements ([7, 6, 5]): [5, 6, 7, 4, 3, 2, 1].
Reverse the remaining elements ([4, 3, 2, 1]): [5, 6, 7, 1, 2, 3, 4].
Thus, the array is rotated right by 3 steps to [5, 6, 7, 1, 2, 3, 4].
'''
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """ Rotates the array 'nums' to the right by 'k' steps in-place. """
        k = k % len(nums)  # Ensure 'k' is within the bounds of the array's length.
        l, r = 0, len(nums) - 1 # Step 1: Reverse the entire array. # noqa: E741
        while l < r:            
            nums[l], nums[r] = nums[r], nums[l] # Swap elements at positions 'l' and 'r'.            
            l, r = l + 1, r - 1 # Move 'l' forward and 'r' backward. # noqa: E741                
        l, r = 0, k - 1  # Step 2: Reverse the first 'k' elements. # noqa: E741
        while l < r:            
            nums[l], nums[r] = nums[r], nums[l] # Swap elements at positions 'l' and 'r'.            
            l, r = l + 1, r - 1 # Move 'l' forward and 'r' backward. # noqa: E741                
        l, r = k, len(nums) - 1  # Step 3: Reverse the remaining elements from index 'k' to the end. # noqa: E741
        while l < r:          
            nums[l], nums[r] = nums[r], nums[l]   # Swap elements at positions 'l' and 'r'.            
            l, r = l + 1, r - 1  # Move 'l' forward and 'r' backward. # noqa: E741