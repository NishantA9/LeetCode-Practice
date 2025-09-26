from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1  # Initialize left and right pointers
        while left <= right:
            mid = left + (right - left) // 2  # Find the middle index
            if nums[mid] == target:
                return True  # Found the target
            if nums[left] < nums[mid]:  # Left portion is sorted
                if nums[left] <= target < nums[mid]:  # Target in left sorted part
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:  # Right portion is sorted
                if nums[mid] < target <= nums[right]:  # Target in right sorted part
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1  # Skip duplicate
        return False  # Target not found