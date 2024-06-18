from typing import List
import heapq

class Solution:
    # minimum of maximum value alone the path
    # O(MNlogMN) O(MN)
    def swimInWater(self, grid: List[List[int]]) -> int:
        seen = set()
        seen.add((0, 0))
        res = 0
        q = [(grid[0][0], 0, 0)]
        n = len(grid)

        while q:
            v, i, j = heapq.heappop(q)
            res = max(res, v)
            if i == j == len(grid) - 1:
                return res
        
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                    seen.add((x, y))
                    heapq.heappush(q, (grid[x][y], x, y))