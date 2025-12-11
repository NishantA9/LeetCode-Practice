class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x  # Initialize left and right pointers for binary search
        res = 0      # Store the result (integer part of sqrt)
        while left <= right:
            m = left + ((right - left) // 2)  # Find the middle value
            if m**2 > x:
                right = m - 1  # If m squared is too big, search left half
            elif m**2 < x:
                left = m + 1  # If m squared is too small, search right half
                res = m    # Update result to current m
            else:
                return m  # Found exact square root
        return res  # Return the integer part of sqrt