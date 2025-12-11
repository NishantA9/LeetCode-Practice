class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1  # one = ways to reach step (i-1), two = ways to reach step (i-2)
        for i in range(n - 1):  # Repeat n-1 times
            temp = one          # Store current 'one'
            one = one + two     # Update 'one' to sum of previous two steps
            two = temp          # Update 'two' to previous 'one'
        return one  # 'one' will now hold the number of ways to reach step n