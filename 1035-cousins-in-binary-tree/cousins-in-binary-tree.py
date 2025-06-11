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
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        queue = deque([root])
        d = dict()
        depth = 0
        d1 = dict()
        prev = root
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                prev = node
                d[node.val] = depth
                if node.left:
                    d1[node.left.val] = prev
                    queue.append(node.left)
                if node.right:
                    d1[node.right.val] = prev
                    queue.append(node.right)
            if x in d and y in d and d[x] == d[y] and d1[x] != d1[y]:
                return True
        return False

        # def f(node, val, depth):
        #     if not node:
        #         return (None, None)
        #     if node.left and node.left.val == val:
        #         return (depth, node)
        #     if node.right and node.right.val == val:
        #         return (depth, node)
        #     return f(node.left, val, depth + 1) or f(node.right, val, depth + 1)
        # h1, p1 = f(root, x, 0)
        # h2, p2 = f(root, y, 0)
        
        # return h1 == h2 and p1 != p2
        
# @lc code=end

