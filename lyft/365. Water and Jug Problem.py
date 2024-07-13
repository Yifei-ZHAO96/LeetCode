from typing import List
from collections import deque

class Solution:
    # O(XY) O(XY)
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        
        q = deque([(0, 0)])
        seen = set()
        
        while q:
            i, j = q.popleft()
            
            if i + j == target:
                return True
            
            seen.add((i, j))
            
            # empty i
            if (0, j) not in seen:
                q.append((0, j))
                
            # empty j
            if (i, 0) not in seen:
                q.append((i, 0))
            
            # fill i
            if (x, j) not in seen:
                q.append((x, j))
                
            # fill j
            if (i, y) not in seen:
                q.append((i, y))
            
            # pour i -> j
            ii = max(0, i + j - y)
            jj = min(y, i + j)
            if (ii, jj) not in seen:
                q.append((ii, jj))
            
            # pour j -> i
            jj = max(0, i + j - y)
            ii = min(x, i + j)
            if (ii, jj) not in seen:
                q.append((ii, jj))

        return False