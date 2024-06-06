from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(N) O(N)
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []

        # post-order
        def dfs(root):
            if not root:
                return None
            
            root.left = dfs(root.left) # return root node of the left branch
            root.right = dfs(root.right) # return root node of the right branch
            
            if root.val in to_delete:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)
                
                return None # remove current node
            
            return root
        
        dfs(root)
        if root.val not in to_delete:
            res.append(root)
        
        return res