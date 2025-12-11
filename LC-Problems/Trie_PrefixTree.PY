class TrieNode:
    def __init__(self):
        self.children = {}       # Dictionary to store child nodes
        self.endOfWord = False   # Marks end of a complete word

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()   # Initialize the root of Trie

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:       # If char doesn't exist, add it
                cur.children[c] = TrieNode()
            cur = cur.children[c]           # Move to the next node
        cur.endOfWord = True                # Mark the end of the word

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:       # If char not found, word doesn't exist
                return False
            cur = cur.children[c]
        return cur.endOfWord                # True only if it's a complete word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:       # If prefix char not found
                return False
            cur = cur.children[c]
        return True                         # Prefix exists in Trie