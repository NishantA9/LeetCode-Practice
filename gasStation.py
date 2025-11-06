from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # If the total gas available is less than the total cost, it's impossible to complete the circuit
            return -1
        total = 0  # Keeps track of the total fuel balance while traversing the stations
        res = 0    # This is the index of the potential starting station
        for i in range(len(gas)): # Iterate over all gas stations
            total += (gas[i] - cost[i]) # Update the total balance at each station
            if total < 0: # If the balance is negative, we can't complete the journey starting from the current station or any station before it
                total = 0 # Reset the total and update the potential starting station to i + 1
                res = i + 1
        return res # Return the index of the starting station