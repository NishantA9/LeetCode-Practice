from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # 'k' keeps track of the position to place non-val elements

        # Iterate through each element in the list
        for i in range(len(nums)):
            # If the current element is not equal to the value we want to remove
            if nums[i] != val:
                # Place the non-val element at index 'k'
                nums[k] = nums[i]
                # Move the 'k' pointer forward for the next non-val element
                k += 1

        # Return the number of elements that are not equal to val
        return k
