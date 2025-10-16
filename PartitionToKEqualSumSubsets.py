from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)  # Sum of all numbers
        if total % k != 0:  # If total not divisible by k, can't partition equally
            return False

        nums.sort(reverse=True)  # Place larger numbers first to help pruning
        target = total // k  # Each subset must sum to this target
        # Quick fail: largest number greater than target -> impossible
        if nums and nums[0] > target:
            return False

        used = [False] * len(nums)  # Track which numbers are already placed

        def backtrack(start: int, groups_remaining: int, current_sum: int) -> bool:
            # If no groups left to fill, success
            if groups_remaining == 0:
                return True

            # When current group reaches target, move to build next group
            if current_sum == target:
                return backtrack(0, groups_remaining - 1, 0)

            # Try to fill current group starting from index `start`
            for j in range(start, len(nums)):
                # Skip used numbers or those that would overflow the target
                if used[j] or current_sum + nums[j] > target:
                    continue

                used[j] = True
                # Recurse: try to place next number
                if backtrack(j + 1, groups_remaining, current_sum + nums[j]):
                    return True
                used[j] = False

                # Prune: if placing nums[j] at empty position didn't lead to solution,
                # no need to try other numbers at this empty position (symmetry)
                if current_sum == 0:
                    return False

            return False

        return backtrack(0, k, 0)