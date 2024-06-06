import collections
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    # 
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        uf = UnionFind(len(vals))

        tree = collections.defaultdict(list)
        # Using a hashmap of set to get the nodes with the same value easily.
        val2Nodes = collections.defaultdict(set)
        # O(E) O(E)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
            val2Nodes[vals[s]].add(s)
            val2Nodes[vals[e]].add(e)
        
        # Include the one node path in the result, because it is not calculated when we do comb(n,r).
        res = len(vals)
        
        # Sort the value, and start to union the nodes with the current v that we are checking and their neighbors (have smaller values than the current v).
        # O(N logN) O(N)
        for v in sorted(val2Nodes.keys()):
            # nodes with the same value
            for node in val2Nodes[v]:
                # neighbor of each node
                for nei in tree[node]:
                    if vals[nei] <= v:
                        # O(alpha(N))
                        uf.union(node, nei)
            
            # For each group, we need to count the number of elements with value==v in this group.
            groupCount = collections.defaultdict(int)
            for node in val2Nodes[v]:
                groupCount[uf.find(node)] += 1
                
            for root in groupCount.keys():
                # The following two lines are doing the same thing
                # If there are n number of nodes that have value==v in the a group. 
                # The number of paths is the number of combinations for selecting 2 elements from n elements (repetitions are not allowed).
                
                # res += comb(groupCount[root], 2)
                res += groupCount[root] * (groupCount[root]-1) // 2
        
        return res