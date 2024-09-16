import random

class RandomizedSet:

    def __init__(self):
        # Initialize an empty dictionary/hashmap to store the values and their corresponding indices in the list
        self.numMap = {}  
        # Initialize an empty list to store the values in the set
        self.numList = []  

    def insert(self, val: int) -> bool:
        # Check if the value is not already in the set (i.e., not in the dictionary/hashmap)
        res = val not in self.numMap  
        if res:
            # If the value is not in the set, add it to the dictionary/hashmap with its index in the list
            self.numMap[val] = len(self.numList)  
            # Add the value to the end of the list
            self.numList.append(val)  
        # Return True if the value was successfully inserted, otherwise False
        return res  

    def remove(self, val: int) -> bool:
        # Check if the value is in the set (i.e., in the dictionary/hashmap)
        res = val in self.numMap  
        if res:
            # Get the index of the value in the list
            idx = self.numMap[val]  
            # Get the last value in the list
            lastVal = self.numList[-1]  
            # Move the last value to the index of the value being removed
            self.numList[idx] = lastVal  
            # Remove the last value from the list
            self.numList.pop()  
            # Update the dictionary/hashmap to reflect the new index of the last value
            self.numMap[lastVal] = idx  
            # Remove the value from the dictionary/hashmap
            del self.numMap[val]  
        # Return True if the value was successfully removed, otherwise False
        return res  

    def getRandom(self) -> int:
        # Randomly select and return a value from the list
        return random.choice(self.numList)
