class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []  # collect letters in reverse order
        while columnNumber > 0:  # process until all digits handled
            columnNumber -= 1  # make 0-indexed for modulo
            offset = columnNumber % 26  # offset 0..25 -> 'A'..'Z'
            res += chr(ord('A') + offset)  # append corresponding letter
            columnNumber //= 26  # move to next place value
        return ''.join(reversed(res))  # reverse collected letters and join