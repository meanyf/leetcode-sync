# Definition for a binary tree node.
try:
    TreeNode
except NameError:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return depth
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
        return dfs(root, 0)