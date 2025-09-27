# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       return 0

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()  # Get the length of the mountain array

        # Find the peak index using binary search
        left, right = 1, length - 2  # Peak can't be at the ends
        while left <= right:
            mid = (left + right) // 2
            left_val = mountainArr.get(mid - 1)
            mid_val = mountainArr.get(mid)
            right_val = mountainArr.get(mid + 1)
            if left_val < mid_val < right_val:  # Ascending slope
                left = mid + 1
            elif left_val > mid_val > right_val:  # Descending slope
                right = mid - 1
            else:  # Found the peak
                break
        peak = mid  # Store the peak index

        # Search left (increasing) portion using binary search
        left, right = 0, peak - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val < target:
                left = mid + 1  # Move right
            elif val > target:
                right = mid - 1  # Move left
            else:
                return mid  # Found target

        # Search right (decreasing) portion using binary search
        left, right = peak, length - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val > target:
                left = mid + 1  # Move right (since decreasing)
            elif val < target:
                right = mid - 1  # Move left
            else:
                return mid  # Found target

        return -1  # Target not found