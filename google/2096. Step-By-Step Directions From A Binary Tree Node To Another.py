from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(N) O(N)
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def lca(root):
            if not root:
                return
            
            if root.val in [startValue, destValue]:
                return root
            
            left = lca(root.left)
            right = lca(root.right)

            if left and right:
                return root
            
            return left or right
        
        node_lca = lca(root)
        path_s = ""
        path_e = ""
        stack = [(node_lca, "")]

        while stack:
            node, path = stack.pop()
            if not node:
                continue

            if node.val == startValue:
                path_s = path
            elif node.val == destValue:
                path_e = path

            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + 'R'))
        
        return 'U' * len(path_s) + path_e