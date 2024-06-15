from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # O(MN) O(1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, frist_y = i, j
        
        bfs_q = deque()
        # O(MN) O(MN)
        self.dfs(grid, first_x, frist_y, bfs_q)

        step = 0
        visited = set()

        # O(MN) O(MN)
        while bfs_q:
            len_q = len(bfs_q)
            for _ in range(len_q):
                x, y = bfs_q.popleft()

                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1:
                        return step
                    elif 0 <= xx < m and 0 <= yy < n and grid[xx][yy] != 0 or (xx, yy) in visited:
                        continue
                    elif 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 0:
                        visited.add((xx, yy))
                        bfs_q.append((xx, yy))
            
            step += 1
        
        return -1
    
    def dfs(self, grid, x, y, bfs_q):
        m, n = len(grid), len(grid[0])
        bfs_q.append((x, y))
        grid[x][y] = 2

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1:
                self.dfs(grid, xx, yy, bfs_q)
