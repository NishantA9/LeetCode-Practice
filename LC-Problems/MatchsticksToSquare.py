from typing import List
#sol 1 easy to understand 
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:        
        l = sum(matchsticks) // 4 # Step 1: Each side of the square should have equal length  # noqa: E741
        s = [0] * 4 # Step 2: Create 4 sides initialized to 0
        if sum(matchsticks) / 4 != l: return False # Step 3: If total length is not divisible by 4, cannot form a square  # noqa: E701
        matchsticks.sort(reverse=True)  # Step 4: Sort in descending order (important optimization) We try placing bigger sticks first → reduces unnecessary recursion      
        def dfs(i): # Backtracking function                       
            if i == len(matchsticks): return True  # Base case: if all matchsticks are used successfully  # noqa: E701
            for j in range(4): # Try placing current matchstick in each of the 4 sides                
                if s[j] + matchsticks[i] <= l: # Check if adding this matchstick keeps side length <= target                    
                    s[j] += matchsticks[i] # Choose: add matchstick to this side                    
                    if dfs(i + 1): return True # Explore: move to next matchstick  # noqa: E701
                    s[j] -= matchsticks[i] # Backtrack: remove matchstick (undo the choice)            
            return False # If no valid placement found, return False        
        return dfs(0) # Start recursion from first matchstick
    
# sol 2 
class Solution2:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)  # total length of all matchsticks
        if total_length % 4 != 0:  # must be divisible into 4 equal sides
            return False
        target = total_length // 4  # length each side must reach
        sides = [0] * 4  # current lengths of the 4 sides
        # sort descending to place large sticks first (prunes search faster)
        matchsticks.sort(reverse=True)
        def dfs(index: int) -> bool:
            # If we've placed all matchsticks, check success
            if index == len(matchsticks):
                return True
            stick = matchsticks[index]  # current stick length
            for side_id in range(4):
                # Try to place stick on side `side_id` if it doesn't exceed target
                if sides[side_id] + stick <= target:
                    sides[side_id] += stick  # place stick
                    if dfs(index + 1):  # continue with next stick
                        return True
                    sides[side_id] -= stick  # backtrack
                # Optimization: if this side was 0 before placing the stick,
                # placing it into other empty sides will be symmetric — break to avoid duplicates
                if sides[side_id] == 0:
                    break
            return False
        return dfs(0)