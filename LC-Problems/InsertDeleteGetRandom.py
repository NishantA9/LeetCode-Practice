import random
class RandomizedSet:
    def __init__(self):
        self.numMap = {}  # Initialize an empty dictionary/hashmap to store the values and their corresponding indices in the list
        self.numList = [] # Initialize an empty list to store the values in the set

    def insert(self, val: int) -> bool:
        res = val not in self.numMap  # Check if the value is not already in the set (i.e., not in the dictionary/hashmap)
        if res:
            self.numMap[val] = len(self.numList) # If the value is not in the set, add it to the dictionary/hashmap with its index in the list
            self.numList.append(val) # Add the value to the end of the list
        return res # Return True if the value was successfully inserted, otherwise False

    def remove(self, val: int) -> bool:
        res = val in self.numMap  # Check if the value is in the set (i.e., in the dictionary/hashmap)
        if res:
            idx = self.numMap[val]  # Get the index of the value in the list 
            lastVal = self.numList[-1]  # Get the last value in the list
            self.numList[idx] = lastVal  # Move the last value to the index of the value being removed
            self.numList.pop() # Remove the last value from the list  
            self.numMap[lastVal] = idx # Update the dictionary/hashmap to reflect the new index of the last value  
            del self.numMap[val] # Remove the value from the dictionary/hashmap
        return res # Return True if the value was successfully removed, otherwise False
 
    def getRandom(self) -> int:
        return random.choice(self.numList) # Randomly select and return a value from the list