#What is palindrome?
#A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string to hold only alphanumeric characters
        newStr = ""
        
        # Loop through each character in the input string
        for c in s:
            if c.isalnum():  # Check if the character is alphanumeric (letter or number)
                newStr += c.lower()  # Convert to lowercase and add to newStr
        
        # Check if the cleaned string is equal to its reverse
        # This checks if the string is a palindrome
        return newStr == newStr[::-1]  # newStr[::-1] creates a reversed version of newStr


# -----------------------------
# Two Pointers Approach

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize two pointers: left (l) at the start and right (r) at the end of the string  # noqa: E741
        
        # Loop until the two pointers meet in the middle
        while l < r:
            # Move the left pointer to the right while the current character is not alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1  # Increment the left pointer  # noqa: E741
            
            # Move the right pointer to the left while the current character is not alphanumeric
            while r > l and not self.alphaNum(s[r]):
                r -= 1  # Decrement the right pointer
            
            # Compare the characters at the left and right pointers (ignoring case)
            if s[l].lower() != s[r].lower():
                return False  # If they are not the same, it's not a palindrome
            
            # Move the pointers closer towards the center
            l, r = l + 1, r - 1  # noqa: E741
        
        return True  # If no mismatches are found, the string is a palindrome
    
    # Helper function to check if a character is alphanumeric without using built-in isalnum()
    def alphaNum(self, c):
        # Check if the character is a letter (uppercase or lowercase) or a number
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
