class TreeNode:
    def __init__(self, val=-1, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        pass
    
    # O(N) O(N)
    def findLeaves(self, root):
        
        results = []
        
        def dfs(node):
            if not node:
                return -1
            
            max_depth = max(dfs(node.left), dfs(node.right)) + 1
            
            if max_depth >= len(results):
                results.append([])

            results[max_depth].append(node.val)
            
            return max_depth
        
        dfs(root)
        return results
            
# Example usage
# Construct the tree
#      1
#     / \
#    2   3
#   / \     
#  4   5    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create a solution instance
solution = Solution()
# Find leaves
leaves = solution.findLeaves(root)
print(leaves)  # Output: [[4, 5, 3], [2], [1]]