#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        stack = [root]
        mn = float('inf')
        while stack:
            node = stack.pop()
            if node.right and node.left:
                if node.val != node.right.val:
                    mn = min(mn, node.right.val)
                if node.val != node.left.val:
                    mn = min(mn, node.left.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return mn if mn < float('inf') else -1
        
        # def dfs(node):
        #     if not node:
        #         return [float('inf')]
        #     return [node.val] + dfs(node.left) + dfs(node.right)
        # s = set(dfs(root))
        # print(s)
        # if len(s) > 2:
        #     return sorted(list(s))[1]
        # else:
        #     return -1
# @lc code=end

