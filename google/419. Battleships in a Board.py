from typing import List

class Solution:
    # O(MN) O(1)
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0

        for i in range(m):
            for j in range(n):
                # check the end
                if board[i][j] == 'X' and (i == m - 1 or board[i+1][j] == '.') and (j == n - 1 or board[i][j+1] == '.'):
                    res += 1
        
        return res