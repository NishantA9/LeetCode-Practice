from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 'last' is the index of the last position to fill in nums1
        last = m + n - 1  # This represents the last index of nums1

        # Merge the two arrays in reverse order (starting from the back)
        # Iterate while both arrays still have elements to compare
        while m > 0 and n > 0:
            # Compare the last elements of both arrays
            if nums1[m - 1] > nums2[n - 1]:
                # If nums1's element is larger, place it at the current 'last' position
                nums1[last] = nums1[m - 1]
                m -= 1  # Move the pointer in nums1 to the left (previous element)
            else:
                # Otherwise, place nums2's element at the current 'last' position
                nums1[last] = nums2[n - 1]
                n -= 1  # Move the pointer in nums2 to the left (previous element)
            last -= 1  # Move the 'last' pointer to the left

        # If any elements are left in nums2 (nums1's elements are already in place)
        while n > 0:
            nums1[last] = nums2[n - 1]  # Place leftover elements from nums2
            n, last = n - 1, last - 1  # Move both pointers to the left
