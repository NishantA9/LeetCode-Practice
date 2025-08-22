
from typing import List
# Solution class to sort an array using merge sort
class Solution: 
    def sortArray(self, nums: List[int]) -> List[int]:
        # Helper function to merge two sorted halves of arr
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1 : R+1]  # Split array into left and right
            i, j, k = L, 0, 0  # i: main array index, j: left index, k: right index
            # Merge elements from left and right into arr
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            # Copy any remaining elements from left
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            # Copy any remaining elements from right
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
        
        # Recursive merge sort function
        def mergeSort(arr, l, r):  # noqa: E741
            if l == r:
                return arr  # Base case: one element
            m = (l + r) // 2  # Find middle
            mergeSort(arr, l, m)  # Sort left half
            mergeSort(arr, m+1, r)  # Sort right half
            merge(arr, l, m, r)  # Merge sorted halves
            return arr

        # Call mergeSort on the whole array
        mergeSort(nums, 0, len(nums) - 1)
        return nums  # Return sorted array