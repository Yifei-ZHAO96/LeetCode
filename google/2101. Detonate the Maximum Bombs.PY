import collections
from typing import List

class Solution:
    # BFS
    # O(V ** 2 + V * E) O(V + E)
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        neighbors = collections.defaultdict(list)
        # O(V ** 2)
        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, rj) in enumerate(bombs):
                if i == j:
                    continue
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= ri ** 2:
                    neighbors[i].append(j)
        
        res = 0
        # O(V)
        for i in range(len(bombs)):
            q = deque([i])
            seen = {i}

            while q:
                len_q = len(q)
                for _ in range(len_q):
                    b = q.popleft()
                    
                    # O(E)
                    for n in neighbors[b]:
                        if n not in seen:
                            seen.add(n)
                            q.append(n)
                    
                    if len(seen) == len(bombs):
                        return len(seen)
                    
                    res = max(res, len(seen))
        
        return res
