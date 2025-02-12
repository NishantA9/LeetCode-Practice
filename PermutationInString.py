class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False  # Edge case # If s1 is longer than s2, it is impossible for s1's permutation to exist in s2
        s1Count, s2Count = [0] * 26, [0] * 26 # Initialize frequency counts for both strings Using arrays of size 26 to represent character counts for 'a' to 'z'
        for i in range(len(s1)):# Populate the frequency counts for s1 and the first window of s2 (length of s1)
            s1Count[ord(s1[i]) - ord('a')] += 1  # Increment count for the character in s1
            s2Count[ord(s2[i]) - ord('a')] += 1  # Increment count for the character in s2
        matches = 0 # Count how many character frequencies match between s1Count and s2Count
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Sliding window to check the rest of s2
        l = 0  # Left pointer for the sliding window  # noqa: E741
        for r in range(len(s1), len(s2)):
            if matches == 26: # If all character frequencies match, s1's permutation exists in s2  
                return True
            
            index = ord(s2[r]) - ord('a')# Add the next character to the window (right pointer)
            s2Count[index] += 1  # Update the count for the character added
            if s1Count[index] == s2Count[index]: # Adjust matches based on whether the new character makes the counts match or not
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:  # Counts no longer match
                matches -= 1

            index = ord(s2[l]) - ord('a') # Remove the left character from the window
            s2Count[index] -= 1  # Update the count for the character removed
            if s1Count[index] == s2Count[index]: # Adjust matches based on whether the removed character makes the counts match or not
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:  # Counts no longer match
                matches -= 1    
            l += 1 # Move the left pointer of the window  # noqa: E741
        return matches == 26 # After the loop, check if all character frequencies match