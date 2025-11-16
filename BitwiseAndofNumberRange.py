class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0  # count how many shifts we've done (bits removed)
        while left != right: # shift both numbers right until they match (finding common high-bit prefix)
            left >>= 1  # drop least-significant bit
            right >>= 1  # drop least-significant bit
            i += 1  # increment shift counter
        return left << i  # shift the common prefix back to original position