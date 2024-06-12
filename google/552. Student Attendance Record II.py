from typing import List

class Solution:
    # O(N) O(N)
    def checkRecord(self, n: int) -> int:
        if n < 2:
            return 3 * n # P, L, A

        mod = 10 ** 9 + 7
        dp = [0] * (n + 1) # without A, number of possible valid attendence
        dp[0] = 1 # ""
        dp[1] = 2 # P, L
        dp[2] = 4 # PP, PL, LP, LL

        # without A
        for i in range(3, n+1):
            # dp[i-1] + P, dp[i-2] + PL, dp[i-3] + PLL
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod
        
        # with A
        res = dp[-1]
        for i in range(1, n+1):
            # dp[i-1], A, dp[n-i]
            res += dp[i-1] * dp[n-i] % mod

        return res % mod