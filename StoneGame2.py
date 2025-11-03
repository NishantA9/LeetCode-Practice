from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(alice, i, M):
            if i == len(piles):
                return 0  # no piles left
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]  # return memoized result
            res = 0 if alice else float("inf")  # maximize for Alice, minimize for Bob
            total = 0  # sum of taken piles in this move
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break  # can't take more piles than remain
                total += piles[i + X - 1]  # add next taken pile
                if alice:
                    # Alice chooses X piles to maximize her score
                    res = max(res, total + dfs(not alice, i + X, max(M, X)))
                else:
                    # Bob chooses to minimize Alice's resulting score
                    res = min(res, dfs(not alice, i + X, max(M, X)))
            dp[(alice, i, M)] = res  # memoize
            return res
        return dfs(True, 0, 1)  # start with Alice at index 0 and M=1