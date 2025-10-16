from typing import List

class Solution:
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