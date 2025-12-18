class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}  # Set of vowel characters
        count = 0
        for i in range(k):  # Count vowels in the first window of size k
            if s[i] in vowels:
                count += 1
        maxC = count  # Initialize max count with the first window's count
        for i in range(k, len(s)):  # Slide the window from k to end of string
            if s[i] in vowels:  # Add vowel count for new character entering window
                count += 1
            if s[i-k] in vowels:  # Subtract vowel count for character leaving window
                count -= 1
            maxC = max(maxC, count)  # Update max count if current window has more vowels
        return maxC