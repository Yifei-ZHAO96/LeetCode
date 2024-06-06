from typing import List
from collections import defaultdict


class UnionFind:
    # O(N)
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n
    
    # O(alpha(N)): inverse Ackermann function, close to constant
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        
        return self.parent[p]
    
    # O(alpha(N)): inverse Ackermann function, close to constant
    def union(self, p, q):
        p_root, q_root = self.find(p), self.find(q)

        if p_root == q_root:
            return

        if self.size[p_root] > self.size[q_root]:
            self.parent[q_root] = p_root
            self.size[p_root] += self.size[q_root]

        elif self.size[p_root] < self.size[q_root]:
            self.parent[p_root] = q_root
            self.size[q_root] += self.size[p_root]

        else:
            self.parent[p_root] = q_root
            self.size[q_root] += 1

        self.count -= 1

    def connected(self, p, q):
        return self.parent[p] == self.parent[q]

    def getCount(self):
        return self.count


class Solution:
    # Union Find
    # O(N logN + N)
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # O(N logN) O(N alpha(N)) O(N)
        logs.sort()
        uf = UnionFind(n)
        # O(N)
        for time, a, b in logs:
            # O(alpha(N))
            uf.union(a, b)
            
            if uf.getCount() == 1:
                return time
        
        return -1


solution = Solution()
logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
n = 4
print(solution.earliestAcq(logs, n))

logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
n = 6
print(solution.earliestAcq(logs, n))