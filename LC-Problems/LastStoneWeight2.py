from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)  # total weight of all stones
        target = stoneSum // 2  # best possible half-sum to minimize difference
        dp = [0] * (target + 1)  # dp[t] = max achievable sum <= t using some stones
        for stone in stones:
            for t in range(target, stone - 1, -1):  # iterate backwards to avoid reuse
                dp[t] = max(dp[t], dp[t - stone] + stone)  # take or skip current stone
        return stoneSum - 2 * dp[target]  # remaining weight = total - 2*best_half