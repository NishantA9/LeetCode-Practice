from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:  # no-op if starting pixel already has target color
            return image
        m, n = len(image), len(image[0])  # matrix dimensions
        dirs = [1,0,-1,0,1]  # direction offsets for 4-neighborhood (right, down, left, up)
        def dfs(r, c, org):
            if not (0 <= r < m) or not (0 <= c < n) or image[r][c] != org:  # bounds and color check
                return
            image[r][c] = color  # fill current pixel
            for d in range(4):
                dfs(r + dirs[d], c + dirs[d + 1], org)  # recurse to neighboring pixels
        dfs(sr, sc, image[sr][sc])  # start DFS from source pixel
        return image  # return modified image