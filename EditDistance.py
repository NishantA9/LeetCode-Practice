class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]  # Step 1: Create DP table initialized with inf
        for j in range(len(word2) + 1): # Step 2: Fill base cases If word1 is empty → need to insert remaining chars of word2
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):        # If word2 is empty → need to delete remaining chars of word1
            cache[i][len(word2)] = len(word1) - i
        for i in range(len(word1) - 1, -1, -1):        # Step 3: Fill the table from bottom to top
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]  # Characters match, move both pointers
                else:
                    cache[i][j] = 1 + min(
                        cache[i + 1][j],     # Delete
                        cache[i][j + 1],     # Insert
                        cache[i + 1][j + 1]  # Replace
                    )
        return cache[0][0]  # Minimum operations to convert full word1 to word2