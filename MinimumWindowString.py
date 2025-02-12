class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""  # Edge case: If t is empty, return an empty string.
        countT, window = {}, {}   # Count the frequency of characters in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Variables to track progress
        have, need = 0, len(countT)  # 'need' is the number of unique characters in t.
        res, resLen = [-1, -1], float("infinity")  # Result and its length.
        l = 0  # Left pointer for the sliding window.  # noqa: E741

        # Iterate through s using the right pointer (r)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)  # Update the count in the window.
            if c in countT and window[c] == countT[c]:# If the current character satisfies the required frequency in t
                have += 1

            while have == need:  # Try to shrink the window from the left
                if (r - l + 1) < resLen: # Update the result if this window is smaller
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1 # Remove the left character from the window
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1  # No longer satisfies the required frequency.
                l += 1  # Move the left pointer. # noqa: E741
        l, r = res  # Extract the result substring # noqa: E741
        return s[l: r+1] if resLen != float("infinity") else ""  # Return the substring or an empty string.