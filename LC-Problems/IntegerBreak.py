class Solution:
    def integerBreak(self, n: int) -> int:        
        dp = {1: 1} # dp[x] stores the maximum product obtainable by breaking x
        def dfs(num):            
            if num in dp: # Return cached result if computed
                return dp[num]
            # If num == n (original number), we may choose not to break it,
            # so start with 0; otherwise start with num itself (no further split)
            dp[num] = 0 if num == n else num            
            for i in range(1, num): # Try splitting num into i and num-i and maximize the product
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        return dfs(n) # Compute and return the best product for n