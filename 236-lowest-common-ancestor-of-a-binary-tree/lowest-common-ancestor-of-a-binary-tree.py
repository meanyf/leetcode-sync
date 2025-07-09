#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return []
        stack = [(root, [])]
        res = []
        res2 = []
        while stack:
            node, lst = stack.pop()
            if node:
                lst.append(node.val)
                if node.val == q.val:
                    res = list(lst)
                if node.val == p.val:
                    res2 = list(lst)
                stack.append((node.right, list(lst)))
                stack.append((node.left, list(lst)))
        mn = min(len(res), len(res2))
        ans = 0
        for i in range(mn):
            if res[i] == res2[i]:
                ans = res[i]
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == ans:
                    return node
                stack.append(node.right)
                stack.append(node.left)
        return None
# @lc code=end

