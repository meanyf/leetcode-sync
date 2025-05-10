#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        h = 0
        par = None
        def f(node, val, depth):
            nonlocal h
            nonlocal par
            if not node:
                return 
            if node.left and node.left.val == val:
                par = node
                h = depth
                return
            if node.right and node.right.val == val:
                par = node
                h = depth
                return
            f(node.left, val, depth + 1)
            f(node.right, val, depth + 1)
        f(root, x, 0)
        h1 = h
        par1 = par
        par = None
        h = 0
        f(root, y, 0)
        if par is None or par1 is None:
            return False
        return h == h1 and par1 != par
        
# @lc code=end

