from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
# dp[i] stores the best score difference current player can achieve, starting from index i (current player score - opponent score)
        dp = {}
        def dfs(i):
            if i == len(stoneValue): # No stones left => no advantage
                return 0
            if i in dp: # Return cached result if available
                return dp[i]
            res = float('-inf')  # worst possible start
            for j in range(i, min(i + 3, len(stoneValue))): # Try taking 1 to 3 stones (as long as within bounds)
# points taken now = sum(stoneValue[i:j+1]) opponent's best from j+1 is dfs(j+1), so net gain = taken - opponent
                res = max(res, sum(stoneValue[i:j + 1]) - dfs(j + 1))
            dp[i] = res  # memoize result
            return res
        return "Alice" if dfs(0) > 0 else "Bob" if dfs(0) < 0 else "Tied" # If score difference >0 Alice wins, <0 Bob wins, else tie