#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        lst2 = []
        def dfs2(node):
            if not node:
                lst2.append(None)
                return None
            lst2.append(node.val)
            dfs2(node.left)
            dfs2(node.right)
        dfs2(subRoot)
        n = len(lst2)
        print(n)
        print(lst2)
        y = False
        
        def dfs(node):
            nonlocal y 
            if not node:
                return [None]
            lst = [node.val] + dfs(node.left) + dfs(node.right)
            if lst == lst2:
                y = True
            return lst
        lst = dfs(root)
        print(lst)

        return y or lst == lst2

# @lc code=end

