from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""  # left, right pointers; best length; previous comparison
        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)  # extend turbulent window when pattern alternates
                r += 1  # move right pointer
                prev = ">"  # record last comparison was '>'
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)  # extend window for '<' pattern
                r += 1
                prev = "<"  # record last comparison was '<'
            else:
                # If equal, advance right; otherwise reset window to start from previous element
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1  # new left is one before right
                prev = ""  # reset previous comparison
        return res  # maximum turbulent subarray length