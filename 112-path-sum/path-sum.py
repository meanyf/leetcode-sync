#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        yes = False
        def dfs(node, sm, depth):
            nonlocal yes
            if not node:
                return 0
            sm += node.val
            if not node.left and not node.right:
                if sm == targetSum and depth >= 1:
                    yes = True
                
            dfs(node.left, sm, depth + 1)
            dfs(node.right, sm, depth + 1)
        dfs(root, 0, 0)
        return yes
# @lc code=end

