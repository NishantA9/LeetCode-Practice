class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]    # Initialize first three numbers of tribonacci sequence
        if n < 3:   # Handle base cases for n < 3
            return t[n]
        for i in range(3, n + 1):   # Calculate tribonacci numbers using rolling array of size 3
            t[i % 3] = sum(t)  # Next number is sum of previous three
        return t[n % 3]  # Return the nth tribonacci number