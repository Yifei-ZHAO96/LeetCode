from typing import List
import heapq

class Solution:
    # O(N logK) O(K)
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        requests = [0] * k

        # O(N)
        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                # O(logK)
                _, id = heapq.heappop(busy)
                heapq.heappush(available, i + (id - i) % k) # 利用 Python 负数取模变成同余的非负数的性质
            
            if not available:
                continue
            
            id = heapq.heappop(available) % k
            heapq.heappush(busy, (start + duration, id))
            requests[id] += 1
        
        max_req = max(requests)
        return [i for i in range(k) if requests[i] == max_req]
