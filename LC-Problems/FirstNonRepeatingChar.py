def firstUniqueChar(s):
    count = {}     # Initialize a dictionary to count the frequency of each character
    for c in s:     # First pass: count the occurrences of each character in the string
        count[c] = 1 + count.get(c, 0)
    for i, c in enumerate(s):     # Second pass: iterate through the string to find the first character with count 1
        if count[c] == 1:
            return i
    return -1     # If no unique character is found, return -1