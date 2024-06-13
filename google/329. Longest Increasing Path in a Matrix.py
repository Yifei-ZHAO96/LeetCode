from typing import List

class Solution:
    # O(MN) O(MN)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 1
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):

                res = max(res, self.dfs(matrix, i, j, dp))
        
        return res
    

    def dfs(self, board, i, j, dp):
        if dp[i][j]:
            return dp[i][j]
        
        m, n = len(board), len(board[0])
        dp[i][j] = max(
            self.dfs(board, i+1, j, dp) if i < m-1 and board[i+1][j] > board[i][j] else 0,
            self.dfs(board, i-1, j, dp) if i > 0 and board[i-1][j] > board[i][j] else 0,
            self.dfs(board, i, j+1, dp) if j < n-1 and board[i][j+1] > board[i][j] else 0,
            self.dfs(board, i, j-1, dp) if j > 0 and board[i][j-1] > board[i][j] else 0,
        ) + 1

        return dp[i][j]