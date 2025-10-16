from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Count incoming and outgoing trust relationships
        # incoming[x] = number of people who trust person x
        # outgoing[x] = number of people that person x trusts
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        # Process each trust relationship
        for src, dst in trust:
            outgoing[src] += 1  # src trusts someone
            incoming[dst] += 1   # dst is trusted by someone

        # Town judge properties:
        # 1. Trusts nobody (outgoing[judge] = 0)
        # 2. Everyone else trusts them (incoming[judge] = n-1)
        # Check each person (1-indexed)
        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i

        # No judge found
        return -1