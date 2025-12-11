from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  # Count frequency of each character
        maxHeap = [[-cnt, char] for char, cnt in count.items()]         # Create max heap using negative counts (since heapq is min heap)
        heapq.heapify(maxHeap)  # Build the heap        
        prev = None  # Store the previously used character to avoid adjacent duplicates
        res = ""     # Result string                
        while maxHeap or prev:    # Continue while there are characters to process         
            if prev and not maxHeap: # If only prev character left but no other characters, impossible to reorganize
                return ""                        
            cnt, char = heapq.heappop(maxHeap) # Pop the most frequent character
            res += char  # Add character to result
            cnt += 1     # Increment count (since we used negative values)                
            if prev:    # Push back the previous character if it exists
                heapq.heappush(maxHeap, prev)
                prev = None            
            if cnt != 0:            # If current character still has remaining count, store it as prev
                prev = [cnt, char]        
        return res