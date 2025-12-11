# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # search range [left, right]
        while left < right:  # binary search until left meets right
            mid = (left + right) // 2  # choose middle
            if isBadVersion(mid):  # noqa: F821
                right = mid  # mid might be first bad, keep it in range
            else:
                left = mid + 1  # mid is good, discard left half
        return left  # left == right == first bad version