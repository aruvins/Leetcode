from collections import Counter
import numpy
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hmap = defaultdict(int)
        for i in range(len(grid)):
            hmap[tuple(grid[i])] += 1
        
        transposed = list(zip(*grid))

        count = 0
        for col in transposed:
            count += hmap[tuple(col)]

        return count

