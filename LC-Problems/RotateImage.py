from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:        
        l, r = 0, len(matrix) - 1  # l and r mark the current layer's left and right column indices # noqa: E741        
        while l < r: # process layers from outermost to innermost            
            for i in range(r - l): # iterate over elements in the current ring (excluding the last one which is handled by swaps)
                top, bottom = l, r                
                topLeft = matrix[top][l + i]  # save top-left value before we overwrite it / save the topleft                
                matrix[top][l + i] = matrix[bottom - i][l] # move bottom-left -> top-left               
                matrix[bottom - i][l] = matrix[bottom][r - i] # move bottom-right -> bottom-left               
                matrix[bottom][r - i] = matrix[top + i][r] # move top-right -> bottom-right        
                matrix[top + i][r] = topLeft # move saved top-left -> top-right
            r -= 1 # finished current outer layer, move inward
            l += 1  # noqa: E741