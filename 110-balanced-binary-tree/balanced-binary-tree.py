#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root, False, 0)]
        d = {}
        while stack:
            node, visited, depth = stack.pop()
            if node:
                if visited:
                    if not node.left and not node.right:
                        d[node] = 0
                    else:
                        d[node] = max(d.get(node.left, 0), d.get(node.right, 0)) + 1
                    if node.left and node.right:
                        if abs(d[node.left] - d[node.right]) > 1:
                            return False
                    if node.left and not node.right:
                        if d[node] > 1:
                            return False
                    if node.right and not node.left:
                        # print(d[node.right])
                        if d[node] > 1:
                            return False
                else:
                    stack.append((node, True, depth))

                # if node.right:
                if node.right:
                    stack.append((node.right, False, depth + 1))
                if node.left:
                # if node.left:
                    stack.append((node.left, False, depth + 1))
        print(d)
        return True
        # x = True
        # def dfs(node):
        #     nonlocal x
        #     if not node:
        #         return 0
        #     left_depth = dfs(node.left)
        #     right_depth = dfs(node.right)
        #     if abs(left_depth - right_depth) > 1:
        #         x = False
        #     return 1 + max(left_depth, right_depth)
        # dfs(root)
        # return x
# @lc code=end

