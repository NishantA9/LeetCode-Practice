from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  #This is a bucket sort solution, Initialize a dictionary/hashmap to count the frequency of each number in nums
        freq = [[] for i in range(len(nums) + 1)] # Initialize a list of empty lists, where the index represents the frequency, The list is sized len(nums) + 1 because the max frequency a number can have is len(nums)
        for n in nums:        # Count the frequency of each number in nums
            count[n] = 1 + count.get(n, 0)  # Increment the count for each number
        for n, c in count.items():        # Group numbers by their frequency in the freq list
            freq[c].append(n)  # Append the number n to the list at index c
        res = [] # Initialize the result list to store the top k frequent elements
        for i in range(len(freq) - 1, 0, -1): # Iterate over the freq list in reverse order (from highest to lowest frequency)
            for n in freq[i]:  # Go through each number with the current frequency
                res.append(n)  # Add the number to the result list
                if len(res) == k:  # If we've added k elements, return the result
                    return res

#-----------------------------------------------------
#another approach using min heap:
class sol2:
    def topk(nums,k):
        count = {}  # Initialize a hashmap to count frequency of each number
        for num in nums:
            count[num] = 1 + count.get(num,0) # Increment count for each number
        heap = [] # Initialize a min heap to keep top k frequent elements
        for num in count:
            heapq.heappush(heap,(count[num],num)) # Push (frequency, number) into heap
            if len(heap) > k:
                heapq.heappop(heap) # If heap exceeds size k, remove the least frequent element
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1]) # Pop number from heap and add to result
        return res # Return final list of top k frequent numbers