class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)  # convert to list so we can remove used letters
        for c in ransomNote:  # iterate required letters
            if c not in magazine:  # letter not available
                return False  # cannot construct ransom note
            else:  # letter available
                magazine.remove(c)  # consume one occurrence
        return True  # all letters found