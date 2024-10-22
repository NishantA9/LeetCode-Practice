from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total gas available is less than the total cost, it's impossible to complete the circuit
        if sum(gas) < sum(cost):
            return -1
        
        total = 0  # Keeps track of the total fuel balance while traversing the stations
        res = 0    # This is the index of the potential starting station

        # Iterate over all gas stations
        for i in range(len(gas)):
            # Update the total balance at each station
            total += (gas[i] - cost[i])
            
            # If the balance is negative, we can't complete the journey starting from the current station or any station before it
            if total < 0:
                # Reset the total and update the potential starting station to i + 1
                total = 0
                res = i + 1
        
        # Return the index of the starting station
        return res
