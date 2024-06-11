import math
from typing import List

class Solution:
    # O(NlogC + N) O(logC + N)
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # f * r^(x-1) < f + changeTime
        # x < log_r(1 + changeTime/r) + 1
        # worst case: r = 2, f = 1, changeTime = 10^5
        upper_bound = math.ceil(math.log2(1 + changeTime)) + 1
        # O(logC) O(logC)
        dp1 = [float('inf')] * upper_bound # min time to complete i laps without changing a tire
        # O(N)
        for f, r in tires:
            total = 0
            current = f
            i = 1

            # O(logC)
            while current < f + changeTime:
                total += current
                current *= r
                dp1[i] = min(dp1[i], total)
                i += 1

        # O(N) O(N)
        dp2 = [-changeTime] + [float('inf')] * numLaps # min time to complete i laps with chaning 0 or more tires
        # O(N)
        for i in range(1, 1 + numLaps):
            # i-j, i-j+1, i-j+2,...,i changeing tire at j then use the same tire until i 
            # O(logC)
            for j in range(1, min(i+1, len(dp1))):
                dp2[i] = min(dp2[i-j] + dp1[j], dp2[i])

            dp2[i] += changeTime

        return dp2[-1]
