class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative, it cannot be a palindrome
        if x < 0:
            return False
        
        # Initialize revNo to store the reversed number
        revNo = 0
        # Copy the value of x to temp for processing
        temp = x

        # Loop to reverse the digits of temp
        while temp != 0:
            # Extract the last digit of temp
            digit = temp % 10
            # Update revNo by adding the extracted digit at the end
            revNo = revNo * 10 + digit
            # Remove the last digit from temp
            temp //= 10
        
        # Check if the reversed number is equal to the original number
        return revNo == x
