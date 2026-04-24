class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.word = False    # Marks end of word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True  # Mark the word's end

    def search(self, word: str) -> bool:
        def dfs(j, root):  # j = index in the word, root = current TrieNode
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":  # wildcard: check all possible children
                    for child in cur.children.values():
                        if dfs(i + 1, child):  # recurse
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word  # return True only if current node is end of a word
        return dfs(0, self.root)
    
# The below is a brute-force implementation that will likely exceed time limits for large inputs, but it serves as a straightforward solution for the problem.
class WordDictionary1:  # Brute-force implementation using a list
    def __init__(self):
        self.store = []  # Store all added words in a list

    def addWord(self, word: str) -> None:
        self.store.append(word)  # Simply append word to the list

    def search(self, word: str) -> bool:
        for w in self.store:  # Check each stored word
            if len(w) != len(word):  # Skip if lengths don't match
                continue
            i = 0
            while i < len(w):  # Iterate through characters
                if w[i] == word[i] or word[i] == '.':  # '.' matches any character
                    i += 1
                else:
                    break
            if i == len(w):  # Found a matching word
                return True
        return False  # No matching word found