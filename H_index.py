from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)  # 'n' is the total number of papers
        paperCount = [0] * (n + 1)  # Initialize an array to count papers with certain citation counts

        # For each citation, increment the count at the respective index in 'paperCount'
        # If a citation is greater than 'n', we treat it as 'n' because the H-index cannot exceed 'n'
        for c in citations:
            paperCount[min(n, c)] += 1
        
        h = n  # Start from the maximum possible H-index, which is 'n'
        papers = paperCount[n]  # Start by counting papers with citation >= 'n'

        # Iterate downwards to find the largest H-index that satisfies the conditions
        while papers < h:
            h -= 1  # Decrease the H-index guess
            papers += paperCount[h]  # Add the count of papers with exactly 'h' citations
        
        return h  # Return the H-index
