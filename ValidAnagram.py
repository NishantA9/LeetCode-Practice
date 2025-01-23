
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # #another method
        # return Counter(s) == Counter(t)
    
        #a follow up question to solve it in O(1) space complexity
        #do a sorting
        # return sorted(s) == sorted(t)
        
        # If lengths of the strings are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Initialize dictionaries/hashmap to count character frequencies, this are the hashmaps
        countS, countT = {}, {}

        # Count frequencies of each character in both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #get the value of the key, if it does not exist, return 0, this removes the key error
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare character frequencies
        for c in countS:
            if countS[c] != countT.get(c, 0): #get the value of the key, if it does not exist, return 0, this removes the key error
                return False

        return True
