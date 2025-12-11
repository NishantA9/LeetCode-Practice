from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0] * n  # dp[r] will store best score difference for subarray ending at r
        for l in reversed(range(n)):  # consider left index from n-1 down to 0
            for r in range(l, n):  # right index from l to n-1
                even = ((r - l) % 2 == 0)  # whose turn? True means current player picks
                left = piles[l] if even else 0  # score if current player picks left
                right = piles[r] if even else 0  # score if current player picks right
                if l == r:
                    dp[r] = left  # single pile
                else:
                    dp[r] = max(dp[r] + left, dp[r - 1] + right)  # choose best of two options
        total = sum(piles)  # total stones
        alice_score = dp[n - 1]  # best score Alice can get
        return alice_score > (total - alice_score)  # Alice wins if she gets more than half