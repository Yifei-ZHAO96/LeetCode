from collections import deque, defaultdict
from typing import List

class Solution:
    # Topo sort
    # O(N) O(N)
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for i, m in zip(range(n), manager):
            if m != -1:
                children[m].append(i)
        
        q = deque([(0, headID)]) # time, manager
        res = 0

        while q:
            t, m = q.popleft()
            res = max(res, t)
            for child in children[m]:
                q.append((t + informTime[m], child))
        
        return res