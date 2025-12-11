from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array for easier duplicate handling
        n = len(nums)  # Get the length of the array
        res: List[List[int]] = []  # List to store the result quadruplets

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate for first number
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate for second number
                    continue

                left, right = j + 1, n - 1  # Two pointers for third and fourth numbers
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]  # Calculate sum of four numbers
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])  # Add to result if match

                        left += 1  # Move left pointer forward
                        while left < right and nums[left] == nums[left - 1]:  # Skip duplicate for third number
                            left += 1

                        right -= 1  # Move right pointer backward
                        # Compare to nums[right + 1] after decrement to skip duplicate for fourth number
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1  # Increase sum by moving left pointer
                    else:
                        right -= 1  # Decrease sum by moving right pointer

        return res  # Return all found quadruplets