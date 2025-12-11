from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}  # map each char to its last index in s
        for i, c in enumerate(s):
            lastIndex[c] = i  # update last occurrence
        res = []  # list of partition sizes
        size = end = 0  # current partition size and current partition end index
        for i, c in enumerate(s):
            size += 1  # include current char
            end = max(end, lastIndex[c])  # extend end if this char's last idx is later
            if i == end:  # reached end of current partition
                res.append(size)  # record partition size
                size = 0  # reset size for next partition
        return res  # list of partition sizes