from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # Initialize the result list with zeros, one for each day
        stack = [] # Stack to keep track of temperatures and their indices Each element in the stack is a pair: [temperature, index]
        for i, t in enumerate(temperatures): # Iterate through the temperatures using their index and value
            while stack and t > stack[-1][0]: # While the stack is not empty and the current temperature is greater than the last stacked temperature
                stackT, stackInd = stack.pop() # Pop the last temperature and its index from the stack
                res[stackInd] = i - stackInd # Calculate the number of days and update the result
            stack.append([t, i]) # Push the current temperature and its index onto the stack
        return res   # Return the final result list