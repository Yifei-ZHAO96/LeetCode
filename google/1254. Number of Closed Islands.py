from typing import List

class Solution:
    # O(MN) O(1)
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            
            if grid[i][j] == 1:
                return True

            grid[i][j] = 1

            left = dfs(i + 1, j)
            right = dfs(i - 1, j)
            up = dfs(i, j + 1)
            down = dfs(i, j - 1)
            
            return left and right and up and down
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    res += 1

        return res