from typing import List

class Solution:
    # O(MN) O(MN)
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = [[0] * (n + 2) for _ in range(m + 2)]
        col = [[0] * (n + 2) for _ in range(m + 2)]
        dia = [[0] * (n + 2) for _ in range(m + 2)]
        a_dia = [[0] * (n + 2) for _ in range(m + 2)]
        
        res = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if mat[i - 1][j - 1]:
                    row[i][j] = row[i-1][j] + 1
                    col[i][j] = col[i][j+1] + 1
                    dia[i][j] = row[i-1][j+1] + 1
                    a_dia[i][j] = row[i-1][j-1] + 1
                    res = max(res,
                              row[i][j],
                              col[i][j],
                              dia[i][j],
                              a_dia[i][j])
        
        return res