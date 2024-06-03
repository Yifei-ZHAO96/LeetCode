import collections
import heapq
from  typing import List

class Solution:
    # O(MlogM + MlogN) O(N+M)
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free = list(range(n))
        occupied = []
        frequency = collections.defaultdict(int)

        # O(MlogM) O(M)
        meetings.sort()

        # O(M)
        for start, end in meetings:
            # O(MlogN)
            while occupied and occupied[0][0] <= start:
                _, room_id, heapq.heappop(occupied)
                heapq.heappush(free, room_id)
            
            if not free:
                pre_end, room_id = heapq.heappop(occupied)
                heapq.heappush(free, room_id)
                end += pre_end - start
            
            room_id = heapq.heappop(free)
            frequency[room_id] += 1
            heapq.heappush(occupied, (end, room_id))

        return max(frequency, key=frequency.get)
