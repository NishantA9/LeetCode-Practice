from collections import defaultdict
from typing import List
class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int) # count occurrences of each point (x,y)
        self.pts = [] # list of added points (preserve order and duplicates)
    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1 # record point occurrence and store in list
        self.pts.append(point)
    def count(self, point: List[int]) -> int:
        res = 0 # Count how many axis-aligned squares can be formed with `point` as one vertex
        px, py = point
        for x, y in self.pts: # iterate through all added points to consider them as the diagonal-opposite corner            
            if (abs(py - y) != abs(px - x)) or x == px or y == py: # need equal side length (abs difference in x == abs difference in y) and corners must not be on the same row or column
                continue   
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)] # the other two required corner coordinates are (x, py) and (px, y) multiply their counts because duplicates increase combinations
        return res