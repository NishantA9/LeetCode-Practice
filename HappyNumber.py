class Solution:
    def isHappy(self, n: int) -> bool:
        # use Floyd's cycle detection (slow/fast pointers) on sequence of sum-of-squares
        slow, fast = n, self.sumOfSquares(n)  # slow moves 1 step, fast moves 2 steps
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)  # fast moves twice
            slow = self.sumOfSquares(slow)  # slow moves once
        return True if fast == 1 else False  # happy if cycle meets at 1

    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10  # extract last digit
            digit = digit ** 2  # square it
            output += digit  # add to running total
            n = n // 10  # drop last digit
        return output  # sum of squares of digits