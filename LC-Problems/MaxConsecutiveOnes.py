class sol:
    def findMaxConsOnes(self, nums):
        current, maxC = 0, 0  # Initialize current streak and max streak counters
        for n in nums:  # Iterate through each number in the array
            if n == 1:  # If the number is 1, increment current streak
                current += 1
                maxC = max(current, maxC)  # Update max streak if current is larger
            else:  # If not 1, reset current streak to 0
                current = 0
        return maxC  # Return the maximum consecutive ones found