from typing import List
import heapq

class Solution:
    # O(N) O(1)
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        small = []
        large = []

        for n in nums:
            heapq.heappush(small, n)
            heapq.heappush(large, -n)

            if len(small) > 4:
                heapq.heappop(small)
                heapq.heappop(large)
        
        return min(abs(a+b) for a, b in zip(sorted(large), sorted(small)[::-1]))