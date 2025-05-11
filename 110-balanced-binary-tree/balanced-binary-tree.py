# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x = True
        def dfs(node):
            nonlocal x
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            if abs(left_depth - right_depth) > 1:
                x = False
            return 1 + max(left_depth, right_depth)
        dfs(root)
        return x