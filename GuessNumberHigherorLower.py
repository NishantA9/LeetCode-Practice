# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass  # Placeholder implementation

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n  # Initialize search range
        while True:
            mid = (left + right) // 2  # Find the middle number
            res = guess(mid)  # Call the guess API
            if res > 0:
                left = mid + 1  # Guess is too low, search higher
            elif res < 0:
                right = mid - 1  # Guess is too high, search lower
            else:
                return mid  # Found the correct number