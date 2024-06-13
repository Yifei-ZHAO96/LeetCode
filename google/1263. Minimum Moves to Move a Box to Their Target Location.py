import heapq
from typing import List

class Solution:
    # O(M**2 N**2 log(M**2 N**2)) O(M**2 N**2)
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        free = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    target = (i, j)
                    free.add((i, j))
                elif grid[i][j] == 'B':
                    box = (i, j)
                    free.add((i, j))
                elif grid[i][j] == '.':
                    free.add((i, j))
                elif grid[i][j] == 'S':
                    player = (i, j)
                    free.add((i, j))
        
        # (moves, player_i, player_j, box_i, box_j)
        q = [(0, player[0], player[1], box[0], box[1])]
        visited = set()

        while q:
            moves, player_i, player_j, box_i, box_j = heapq.heappop(q)
            
            if (box_i, box_j) == target:
                return moves

            if (player_i, player_j, box_i, box_j) in visited: continue
            visited.add((player_i, player_j, box_i, box_j))
            
            # O(M**2 N**2 log(M**2 N**2)) O(M**2 N**2)
            for ii, jj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x = player_i + ii
                y = player_j + jj
                box_x = box_i + ii
                box_y = box_j + jj

                if (x, y) == (box_i, box_j) and (box_x, box_y) in free and (x, y, box_x, box_y) not in visited:
                    heapq.heappush(q, (moves+1, x, y, box_x, box_y))

                elif (x, y) != (box_i, box_j) and (x, y) in free and (x, y, box_i, box_j) not in visited:
                    heapq.heappush(q, (moves, x, y, box_i, box_j))

        return -1
