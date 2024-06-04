from collections import deque
from typing import List

class Solution:
    # O(MNK) O(MNK)
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2: return m + n - 2

        q = deque([(0, 0, k)]) # x, y, k_remain
        seen = set()
        step = 0

        while q:
            len_q = len(q)
            for _ in range(len_q):
                x, y, kk = q.popleft()
                if x == m - 1 and y == n - 1:
                    return step
                
                for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    xx = x + i
                    yy = y + j
                    if (0 <= xx < m) and (0 <= yy < n) and \
                    ((xx, yy, kk - grid[xx][yy]) not in seen) and (kk - grid[xx][yy] >= 0):
                        seen.add((xx, yy, kk - grid[xx][yy]))
                        q.append((xx, yy, kk - grid[xx][yy]))
            
            step += 1
        
        return -1