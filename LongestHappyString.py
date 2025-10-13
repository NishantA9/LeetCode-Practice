import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""  # Result string
        maxHeap = []  # Max heap to store characters by frequency     
        # Add characters to heap with negative counts (for max heap behavior)
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:  # Only add characters with positive count
                heapq.heappush(maxHeap, (count, char))
        while maxHeap:
            count, char = heapq.heappop(maxHeap)  # Get most frequent character          
            # Check if adding this character would create 3 consecutive same chars
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:  # No other character available
                    break
                # Use second most frequent character instead
                count2, char2 = heapq.heappop(maxHeap)
                res += char2  # Add the alternative character
                count2 += 1   # Increment count (since we use negative values)
                if count2:    # If still has remaining count
                    heapq.heappush(maxHeap, (count2, char2))
                heapq.heappush(maxHeap, (count, char))  # Put back original char
            else:
                res += char  # Safe to add this character
                count += 1   # Increment count (since we use negative values)
                if count:    # If still has remaining count
                    heapq.heappush(maxHeap, (count, char))
        return res