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
        stack = []
        current = root
        prev_val = None
        while stack or current:
            if current:
                if prev_val is not None:
                    stack.append((current, current.val + prev_val))
                else:
                    stack.append((current, current.val))
                prev_val = stack[-1][1]
                current = current.left
            else:
                if stack:
                    prev_val = stack[-1][1]
                node, val = stack.pop()
                if not node.right and not node.left:
                    if val == targetSum:
                        return True
                current = node.right
            
            
        return False

        # if not root:
        #     return False
        # if not root.left and not root.right:
        #     return root.val == targetSum
        # yes = False
        # def dfs(node, sm):
        #     nonlocal yes
        #     if not node:
        #         return 0
        #     sm += node.val
        #     if not node.left and not node.right:
        #         if sm == targetSum:
        #             yes = True
        #     dfs(node.left, sm)
        #     dfs(node.right, sm)
        # dfs(root, 0)
        # return yes
# @lc code=end

