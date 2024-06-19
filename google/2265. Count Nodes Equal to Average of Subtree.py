# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(N) O(N)
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return [0, 0] # sum and count
            
            left = dfs(node.left)
            right = dfs(node.right)

            count = [node.val + left[0] + right[0], 1 + left[1] + right[1]]
            if count[0] // count[1] == node.val:
                self.res += 1

            return count
        
        dfs(root)

        return self.res