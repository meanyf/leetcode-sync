#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        current = root
        res = []
        mn = float('inf')
        prev = None
        while stack or current:
            if current:
                stack.append(current)
                if current.left:
                    mn = min(mn, abs(current.val - current.left.val))
                current = current.left
            else:
                node = stack.pop()
                if prev and node:
                    mn = min(mn, abs(node.val - prev.val))
                prev = node
                res.append(node.val)
                current = node.right
        return mn
        # if not root:
        #     return 0
        # stack = []
        # current = root
        # res = []
        # while stack or current:
        #     if current:
        #         stack.append(current)
        #         current = current.left
        #     else:
        #         node = stack.pop()
        #         res.append(node.val)
        #         current = node.right
        # mn = abs(res[0] - res[1])
        # for i in range(len(res) - 1):
        #     mn = min(mn, abs(res[i] - res[i + 1]))
        # return mn
        # mn = float('inf')
        # prev = None
        # def dfs(node):
        #     nonlocal prev
        #     nonlocal mn
        #     print(prev)
        #     if not node:
        #         return
        #     dfs(node.left)
        #     if prev is not None:
        #         mn = min(mn, abs(prev - node.val))
        #     prev = node.val
        #     dfs(node.right)
        # dfs(root)
        
        # return mn

# @lc code=end

