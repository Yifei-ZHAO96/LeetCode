from typing import List

class Solution:
    # O(MN) O(N)
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0] # the maximum value for the current row

        for row in points[1:]:
            for j in range(1, n):
                dp[j] = max(dp[j], dp[j-1] - 1)
                dp[-j-1] = max(dp[-j-1], dp[-j] - 1)
            
            for j in range(n):
                dp[j] += row[j]
        
        return max(dp)