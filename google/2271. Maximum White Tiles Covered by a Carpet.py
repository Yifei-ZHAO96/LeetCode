from typing import List


class Solution:
    # Sliding window
    # O(N logN) O(N)
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        r = res = cur = 0
        n = len(tiles)

        for l in range(n):
            if l:
                cur -= tiles[l-1][1] - tiles[l-1][0] + 1
            while r < n and tiles[l][0] + carpetLen > tiles[r][1]:
                cur += tiles[r][1] - tiles[r][0] + 1
                r += 1
            
            if r == n:
                res = max(res, cur)
                return res
            else:
                extra = max(0, tiles[l][0] + carpetLen - tiles[r][0])
                res = max(res, extra + cur)
        
        return res