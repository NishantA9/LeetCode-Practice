from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # 'k' keeps track of the position to place non-val elements
        for i in range(len(nums)): # Iterate through each element in the list
            if nums[i] != val:  # If the current element is not equal to the value we want to remove
                nums[k] = nums[i]   # Place the non-val element at index 'k'
                k += 1 # Move the 'k' pointer forward for the next non-val element
        return k   # Return the number of elements that are not equal to val