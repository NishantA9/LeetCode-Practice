class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0  # min/max possible '(' count after processing chars
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1  # '(' increases both
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1  # ')' decreases both
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1  # '*' can be '(', ')' or ''
            if leftMax < 0:
                return False  # too many ')' so far
            if leftMin < 0:
                leftMin = 0  # can't have negative minimum, clamp to 0
        return leftMin == 0  # valid if minimum possible open parens is 0