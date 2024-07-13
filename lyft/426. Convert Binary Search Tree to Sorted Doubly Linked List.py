from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = pre = None
        
        def dfs(node):
            nonlocal head, pre
            
            if not node:
                return
            
            dfs(node.left)
            
            if not pre:
                head = node
            else:
                pre.right = node
                node.left = pre
            pre = node
            
            dfs(node.right)
        
        dfs(root)
        
        if not root:
            return
        
        head.left = pre
        pre.right = head
        return head