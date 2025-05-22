from collections import Counter
import numpy
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hmap = defaultdict(int)
        for i in range(len(grid)):
            hmap[tuple(grid[i])] += 1
        
        transposed = list(zip(*grid))

        matching = 0
        for col in transposed:
            matching += hmap[tuple(col)]

        return matching

