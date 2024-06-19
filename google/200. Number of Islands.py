from typing import List

class Solution:
    # O(MN) O(MN)
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = '2'

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res