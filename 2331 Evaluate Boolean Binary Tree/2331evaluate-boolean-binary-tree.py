# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            if node.val == 0 or node.val == 1:
                return bool(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == 2:
                return left or right
            if node.val == 3:
                return left and right
        return dfs(root)