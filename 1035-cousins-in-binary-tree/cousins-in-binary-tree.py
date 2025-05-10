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
        def f(node, val, depth):
            if not node:
                return None
            if node.left and node.left.val == val:
                return (depth, node)
            if node.right and node.right.val == val:
                return (depth, node)
            return f(node.left, val, depth + 1) or f(node.right, val, depth + 1)
        ans1 = f(root, x, 0) 
        ans2 = f(root, y, 0)
        if ans1 is None or ans2 is None:
            return False
        h1, p1 = ans1
        h2, p2 = ans2    
        print(h1, p1)
        print(h2, p2)

        return h1 == h2 and p1 != p2
# @lc code=end

