from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}      # character -> TrieNode
        self.isWord = False     # flag to mark complete word

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True       # mark end of word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)     # insert all words into Trie
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, node, word):# base cases: out of bounds, visited, or char not in Trie
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in visit or board[r][c] not in node.children):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)   # found valid word
            dfs(r + 1, c, node, word)            # explore neighbors
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))  # backtrack
        for r in range(ROWS):        # start DFS from each cell
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)