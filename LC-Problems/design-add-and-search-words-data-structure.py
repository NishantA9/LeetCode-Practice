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