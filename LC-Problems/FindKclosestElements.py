from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1  # Two pointers for window
        while right - left >= k:  # Shrink window until size k
            if abs(x - arr[left]) <= abs(x - arr[right]):  # Compare distances to x
                right -= 1  # Remove element farther from x (right side)
            else:
                left += 1  # Remove element farther from x (left side)
        return arr[left:right+1]  # Return the k closest elements