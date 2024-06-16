import collections

class UnionFind: # 时间复杂度: O(n * α(n)), 空间复杂度: O(n)
    def __init__(self, n, rank) -> None:
        self.root = list(range(n))  # roots
        self.size = [0] * n  # size of the root
        self.rank = rank # rank
    
    def find(self, x):
        # find and compress the path
        if x == self.root[x]:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
    
    def union(self, x, y):
        # union
        x_root, y_root = map(self.find, (x, y))
        
        if x_root == y_root:
            return
        
        if self.size[x_root] > self.size[y_root]:
            self.root[y_root] = x_root
            self.update_rank(x_root, x_root, y_root)
            
        elif self.size[x_root] < self.size[y_root]:
            self.root[x_root] = y_root
            self.update_rank(y_root, x_root, y_root)
            
        else:
            self.root[y_root] = x_root
            self.size[x_root] += 1
            self.update_rank(x_root, x_root, y_root)
    
    def update_rank(self, x, y, z):
        # update rank
        self.rank[x] = max(self.rank[y], self.rank[z])

# Time:  O(m * n * log(m * n) + m * n * α(m + n)) = O(m * n * log(m * n))
# Space: O(m * n)
class Solution:
    def matrixRankTransform(self, matrix):
        m, n = len(matrix), len(matrix[0])
        lookup = collections.defaultdict(list) # {value: [(x, y)]}
        
        # O(MN) O(MN)
        for i in range(m):
            for j in range(n):
                lookup[matrix[i][j]].append((i, j))
        
        rank = [0] * (m + n)
        
        # O(MN logMN) O(MN)
        for v in sorted(lookup.keys()):
            new_rank = rank[:] # copy rank
            uf = UnionFind(m + n, new_rank)
            
            # O(MN)
            for i, j in lookup[v]:
                # O(alpha(M+N))
                uf.union(i, j + m) # union same value
            # O(MN)
            for i, j in lookup[v]:
                # O(alpha(M+N))
                matrix[i][j] = rank[i] = rank[j + m] = new_rank[uf.find(i)] + 1 # update rank
        
        return matrix