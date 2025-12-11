def reverseString(s):
    res = ""
    for i in range(len(s) -1,-1,-1): # Start from last index down to 0
        res += s[i]
        print(i, s[i])
    return res

#another method

def rS2(s):
    return s[::-1] #Use slicing (easiest in Python)