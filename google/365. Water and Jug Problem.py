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
            seen.add((i, j))
            if i + j == target:
                return True
            
            # clear i
            if (0, j) not in seen:
                q.append((0, j))
            
            # clear j
            if (i, 0) not in seen:
                q.append((0, j))
            
            # fill i
            if (x, j) not in seen:
                q.append((x, j))
            
            # fill j
            if (i, y) not in seen:
                q.append((i, y))
            
            # pour i -> j
            jj = min(y, i + j)
            ii = max(0, i + j - y)
            if (ii, jj) not in seen:
                q.append((ii, jj))
            
            # pour j -> i
            ii = min(x, i + j)
            jj = max(0, i + j - x)
            if (ii, jj) not in seen:
                q.append((ii, jj))
    
        return False