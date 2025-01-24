class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative, it cannot be a palindrome
        if x < 0:
            return False
        
        revNo = 0 # Initialize revNo to store the reversed number
        temp = x  # Copy the value of x to temp for processing

        # Loop to reverse the digits of temp
        while temp != 0:
            digit = temp % 10 # Extract the last digit of temp
            revNo = revNo * 10 + digit # Update revNo by adding the extracted digit at the end
            temp //= 10 # Remove the last digit from temp
        return revNo == x # Check if the reversed number is equal to the original number
