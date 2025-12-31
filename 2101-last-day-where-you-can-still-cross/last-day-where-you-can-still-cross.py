class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l, r = 1, row * col

        while l < r:
            m = r - (r - l) // 2
            if self.isPossible(row, col, cells, m):
                l = m
            else:
                r = m - 1

        return l

    def isPossible(self, row, col, cells, day):
        grid = [[0] * col for _ in range(row)]
        q = collections.deque()

        for r, c in cells[:day]:
            grid[r - 1][c - 1] = 1

        for i in range(col):
            if not grid[0][i]:
                q.append((0, i))
                grid[0][i] = -1

        while q:
            r, c = q.popleft()
            if r == row - 1:
                return True

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    grid[nr][nc] = -1
                    q.append((nr, nc))

        return False