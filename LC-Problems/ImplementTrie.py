class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes (key: character, value: TrieNode)
        self.children = {}
        # Flag to mark if this node represents end of a word
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        # Initialize Trie with an empty root node
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        # Start from root node
        cur = self.root
        # Build trie by creating nodes for each character
        for c in word:
            # Create new node if character doesn't exist
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node
            cur = cur.children[c]
        # Mark last node as end of word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Start from root node
        cur = self.root
        # Follow path of characters in the word
        for c in word:
            # Return False if character not found
            if c not in cur.children:
                return False
            # Move to next character's node
            cur = cur.children[c]
        # Word exists only if we reached end of word marker
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start from root node
        cur = self.root
        # Check if prefix path exists in trie
        for c in prefix:
            # Return False if character not found
            if c not in cur.children:
                return False
            # Move to next character's node
            cur = cur.children[c]
        # Return True if we can follow prefix path completely
        return True
        
        