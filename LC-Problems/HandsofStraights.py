from typing import List
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: # If total number of cards isn't divisible by groupSize, we can't form complete groups
            return False
        count = {}  # Dictionary to store the frequency of each card
        for n in hand:
            count[n] = 1 + count.get(n, 0)  # Count each card
        minH = list(count.keys())  # Convert the unique card values into a min-heap for ordered access to the smallest card
        heapq.heapify(minH)
        while minH:  # Keep forming groups starting from the smallest card
            first = minH[0]  # Smallest card available
            for i in range(first, first + groupSize): # Try to form a consecutive group of size groupSize starting from 'first'
                if i not in count:  # If the required card doesn't exist, group can't be formed
                    return False
                count[i] -= 1  # Use one occurrence of the card
                if count[i] == 0:
                    # Only remove from heap if the card is at the top (to preserve min-heap order)
                    if i != minH[0]:  # Trying to pop a card that's not the current top of heap — invalid
                        return False
                    heapq.heappop(minH)  # Remove the used-up card from heap
        return True # All cards grouped successfully