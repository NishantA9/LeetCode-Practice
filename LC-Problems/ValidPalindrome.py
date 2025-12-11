#What is palindrome?
#A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""         # Create a new string to hold only alphanumeric characters
        for c in s:        # Loop through each character in the input string
            if c.isalnum():  # Check if the character is alphanumeric (letter or number)
                newStr += c.lower()  # Convert to lowercase and add to newStr
        # Check if the cleaned string is equal to its reverse, This checks if the string is a palindrome
        return newStr == newStr[::-1]  # newStr[::-1] creates a reversed version of newStr

# -----------------------------
# Two Pointers Approach

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize two pointers: left (l) at the start and right (r) at the end of the string  # noqa: E741
        while l < r:        # Loop until the two pointers meet in the middle
            while l < r and not self.alphaNum(s[l]):            # Move the left pointer to the right while the current character is not alphanumeric
                l += 1  # Increment the left pointer  # noqa: E741
            while r > l and not self.alphaNum(s[r]):            # Move the right pointer to the left while the current character is not alphanumeric
                r -= 1  # Decrement the right pointer
            if s[l].lower() != s[r].lower():            # Compare the characters at the left and right pointers (ignoring case)
                return False  # If they are not the same, it's not a palindrome
            l, r = l + 1, r - 1  # Move the pointers closer towards the center # noqa: E741
        return True  # If no mismatches are found, the string is a palindrome
    
    def alphaNum(self, c):    # Helper function to check if a character is alphanumeric without using built-in isalnum()
        return (ord('A') <= ord(c) <= ord('Z') or         # Check if the character is a letter (uppercase or lowercase) or a number
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

# -----------------------------
#Another 2 pointers approach
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1        # Initialize two pointers at the beginning and end of the string  # noqa: E741
        while l < r:
            while l < r and not s[l].isalnum(): # Move the left pointer forward if current character is not alphanumeric
                l += 1 # noqa: E741
            while r > l and not s[r].isalnum(): # Move the right pointer backward if current character is not alphanumeric
                r -= 1
            if s[l].lower() != s[r].lower():            # Compare the lowercase versions of characters
                return False  # Characters don't match, so it's not a palindrome
            l, r= l+1, r -1  # Move both pointers toward the center # noqa: E741
        return True  # All characters matched — it's a valid palindrome