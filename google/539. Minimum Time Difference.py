from typing import List

class Solution:
    # O(NlogN) O(N)
    def findMinDifference(self, timePoints: List[str]) -> int:
        calc = lambda x: int(x[:2]) * 60 + int(x[-2:])
        time = sorted(map(calc, timePoints))

        min_diff = float('inf')
        for i in range(1, len(time)):
            min_diff = min(min_diff, time[i] - time[i-1])
        
        min_diff = min(min_diff, time[0] + 24 * 60 - time[-1])
        return min_diff