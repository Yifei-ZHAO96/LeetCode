from typing import List
import heapq

class Solution:
    # O(NlogN) O(N)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        res = 0
        
        for s, e in intervals:
            while pq and pq[0] <= s:
                heapq.heappop(pq)
            heapq.heappush(pq, e)
            res = max(res, len(pq))

        return res

intervals = [[0,30],[5,10],[15,20]]
print(Solution().minMeetingRooms(intervals))
intervals = [[7,10],[2,4]]
print(Solution().minMeetingRooms(intervals))
