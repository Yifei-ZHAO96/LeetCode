from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        root = 0
#         在题目要求中，每个节点的值是唯一的，所以一个节点只能被其父节点引用，不能同时被多个节点引用。因此，一个节点的值只能被根节点及其父节点访问，不会被其他非父节点访问。

# 具体来说，根节点的值在整个树结构中只出现一次，而其他节点的值会出现两次：一次作为父节点，一次作为子节点。因此，利用异或运算的性质，我们可以唯一地识别根节点。
        for node in tree:
            root ^= node.val
            for child in node.children:
                root ^= child.val
        
        for node in tree:
            if root == node.val:
                return node
        
        return None