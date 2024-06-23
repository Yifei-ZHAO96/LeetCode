from typing import List
from collections import deque

class Solution:
    # O(N**2 M) O(NM)
    def numSimilarGroups(self, strs: List[str]) -> int:
        # O(M)
        def find_diff(A, B):
            count = 0
            for a, b in zip(A, B):
                if a != b:
                    count += 1
                    if count > 2: break
            
            return count
        
        def bfs(s):
            q = deque([s])

            while q:
                s = q.popleft()
                seen.add(s)
                # O(N)
                for ss in strs:
                    if ss in seen or find_diff(s, ss) != 2: continue
                    q.append(ss)

        def dfs(s):
            seen.add(s)
            for ss in strs:
                if ss in seen or find_diff(s, ss) != 2: continue
                dfs(ss)

        seen = set() # in existing group
        res = 0
        # O(N)
        for s in strs:
            if s in seen: continue
            res += 1
            # bfs(s)
            dfs(s)
        
        return res