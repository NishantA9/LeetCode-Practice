from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2  # Assign shorter array to A and longer to B
        total = len(A) + len(B)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A #Swap to ensure A is the shorter array
        l, r = 0, len(A) - 1 # Binary search on the shorter array  # noqa: E741
        while True:
            i = (l + r) // 2  # Middle of array A
            j = half - i - 2  # Corresponding index in array B
            
            # Calculate boundaries
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright: # Check if partition is valid
                # Median calculation based on total length
                if total % 2:  # Odd length
                    return min(Aright, Bright)
                else:  # Even length
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:             # Adjust binary search
                r = i - 1
            else:
                l = i + 1  # noqa: E741