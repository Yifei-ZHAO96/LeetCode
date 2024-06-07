from typing import List
import collections

class Solution(object):
    # DP
    # O(MN logMN) O(MN)
    def maxIncreasingCells(self, M: List[List[int]]) -> int:
        m, n = len(M), len(M[0])
        value_loc_map = collections.defaultdict(list)
        # O(MN) O(MN)
        for i in range(m):
            for j in range(n):
                value_loc_map[M[i][j]].append((i, j))
        
        row, col = [0] * m, [0] * n
        # O(MN) O(MN)
        dp = [[0] * n for _ in range((m))] # dp[i][j] means the maximum steps can go from the first cell.

        # O(MN logMN) O(MN)
        for v in sorted(value_loc_map.keys()):
            for i, j in value_loc_map[v]:
                dp[i][j] = max(row[i], col[j]) + 1 # M[i][j] is definitely greater than the previous value
            
            for i, j in value_loc_map[v]:
                row[i] = max(row[i], dp[i][j]) # update row, col
                col[j] = max(col[j], dp[i][j])
        
        return max(row)