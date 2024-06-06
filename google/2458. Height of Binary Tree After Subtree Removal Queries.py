import collections
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(N + M) O(N)
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def dfs(root, l):
            if not root:
                return 0
            
            h = 1 + max(dfs(root.left, l + 1), dfs(root.right, l + 1)) # height
            # 记录当前节点的level和高度
            level[root.val] = l # level
            height[root.val] = h

            # 更新当前level的最高和次高的高度
            # update highest and 2nd highest value for the current level
            if top[l][0] < h:
                top[l][0], top[l][1] = h, top[l][0]

            # update 2nd highest value for the current level
            elif top[l][1] < h:
                top[l][1] = h
            
            return h

        top = collections.defaultdict(lambda: [0] * 2)
        level = {}
        height = {}

        dfs(root, 0)

        res = []
        for q in queries:
            # 计算移除节点后的树的高度和level
            l = level[q]
            h = height[q]
            # highest
            if h == top[l][0]:
                res.append(l - 1 + top[l][1])
            else:
                res.append(l - 1 + top[l][0])
            
        return res