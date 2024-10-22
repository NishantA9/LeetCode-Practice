from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []  # This will store the final list of justified lines
        line, length = [], 0  # 'line' stores the current words, 'length' is the total length of words in the current line
        i = 0
        
        # Loop through each word in the list
        while i < len(words):
            # Check if adding the next word exceeds the maxWidth
            if length + len(line) + len(words[i]) > maxWidth:
                # Calculate extra space needed for justification
                extra_space = maxWidth - length
                # Divide spaces evenly between words
                spaces = extra_space // max(1, len(line) - 1)
                # Handle any remainder spaces that need to be distributed from the left
                remainder = extra_space % max(1, len(line) - 1)

                # Distribute spaces between words
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                # Join the line and add it to the result
                res.append("".join(line))
                # Reset line and length for the next line
                line, length = [], 0
            
            # Add the current word to the line
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # Handle the last line (left-justified)
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)  # Calculate the trailing spaces to fill the line
        res.append(last_line + " " * trail_space)  # Append the last line with trailing spaces
        
        return res  # Return the fully justified lines
