class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # Base case: one way to decode an empty string
        def dfs(i):
            if i in dp:
                return dp[i]  # Return cached result
            if s[i] == "0":
                return 0  # '0' is not decodable on its own
            res = dfs(i + 1)            # Option 1: Take one digit
            if (i + 1 < len(s) and 
               (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):            # Option 2: Take two digits if valid (10–26)
                res += dfs(i + 2)
            dp[i] = res  # Cache the result
            return res
        return dfs(0)