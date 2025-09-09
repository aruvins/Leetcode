class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dfs(i,j):
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0

            if i == 0 and j == 0:
                return 1
            
            return dfs(i - 1, j) + dfs(i, j - 1)

        return dfs(m - 1, n - 1)