import math
from typing import List

class Solution:
    # two pointer, sliding window
    # O(NlogN) O(N)
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x, y = location
        res = 0
        extra = 0
        angs = []
        for xx, yy in points:
            if x == xx and y == yy:
                extra += 1
                continue
            angs.append(math.atan2(y - yy, x - xx))
        angs.sort()
        angs += [a + 2.0 * math.pi for a in angs] # cirsular, handle negatives
        print(angs)
        l = 0
        
        angle = math.pi * angle / 180
        for r in range(len(angs)):
            while angs[r] - angs[l] > angle:
                l += 1
            res = max(res, r-l+1)
        return res + extra