class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2  # Add least significant bit to count
            n = n >> 1    # Right shift to process next bit
        return res