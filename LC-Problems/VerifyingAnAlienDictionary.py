from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping of character to its position in alien alphabet
        # e.g., if order = "hlabcdefgijk", then h->0, l->1, a->2, etc.
        order_index = {c: i for i, c in enumerate(order)}

        # Compare each adjacent pair of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Compare characters at each position
            for j in range(len(w1)):
                # If w2 is prefix of w1, w2 should come first (like "app" < "apple")
                if j == len(w2):
                    return False

                # If characters differ, check their order
                if w1[j] != w2[j]:
                    # If char in w1 comes after char in w2 in alien order, wrong order
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    # Found first different char and it's in correct order, move to next pair
                    break
                    
        # All adjacent pairs are in correct order
        return True