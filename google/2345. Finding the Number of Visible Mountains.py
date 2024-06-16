from typing import List
from collections import Counter

class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        coor = [(x - r, x + r) for x, r in peaks]
        coor.sort(key=lambda x: (x[0], x[-1]))
        
        counter = Counter(coor)
        res = 0
        cur = -float('inf')
        
        for l, r in coor:
            if r <= cur:
                continue
            
            cur = r
            if counter[(l, r)] == 1:
                res += 1

        return res
    

peaks = [[2,2],[6,3],[5,4]]
# Output: 2
print(Solution().visibleMountains(peaks))

peaks = [[1,3],[1,3]]
# Output: 0
print(Solution().visibleMountains(peaks))