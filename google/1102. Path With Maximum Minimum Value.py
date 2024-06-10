from typing import List
import heapq


# Dijkstra algorithm solution
class Solution(object):
    # Time:  O(m * n * log(m * n))
    # Space: O(m * n)
    def maximumMinimumPath(self, A: List[List[int]]):
        m, n = len(A), len(A[0])
        seen = set([(0, 0)])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = [(-A[0][0], 0, 0)]
        
        while q:
            v, x, y = heapq.heappop(q)
            if x == m - 1 and y == n - 1:
                return -v
            for i, j in dirs:
                xx = x + i
                yy = y + j
                if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen:
                    seen.add((xx, yy))
                    heapq.heappush(q, (-min(-v, A[xx][yy]), xx, yy))
        
        return -1

grid = [[5,4,5],[1,2,6],[7,4,6]]
print(Solution().maximumMinimumPath(grid))
grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
print(Solution().maximumMinimumPath(grid))
grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
print(Solution().maximumMinimumPath(grid))
