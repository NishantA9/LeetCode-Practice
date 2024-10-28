class Sol:
    def strStr(self, haystack: str, needle: str) -> int:
 # Return 0 if needle is empty, as per problem statement
        if needle == "":
            return 0
        
      # Loop over possible starting indices for the needle within haystack
        for i in range(len(haystack) + 1 - len(needle)):
            
            # for j in range(len(needle)):
            #     if haystack[i + j] != needle[j]:
            #         break
            #     if j == len(needle) - 1:
            #         return i
            
            #leetcode solution
                # Check if the substring from i to i+len(needle) matches needle
            if haystack[i:i + len(needle)] == needle:
                return i # Return the starting index if there's a match
        return -1         # If no match is found, return -1

    
    
    
            