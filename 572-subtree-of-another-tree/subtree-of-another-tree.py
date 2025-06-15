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
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        stack = [root]
        node_sub = None
        node = None
        res = deque()
        while stack:
            node = stack.pop()
            res.append(node)
            if node:
                stack.append(node.right)
                stack.append(node.left)
        stack = [root]
        node_sub = subRoot
        stack_sub = [subRoot]
        while stack or res:
            if stack_sub:
                node_sub = stack_sub.pop()
            
            if stack:
                node = stack.pop()
            else:
                if res:
                    stack = [res[0]]
                    res.popleft()
            if node_sub and not node:
                stack_sub = [subRoot]
            if node:
                if (
    node_sub and node and
    node.val == node_sub.val and
    (not node.left and not node_sub.left or node.left and node_sub.left and node.left.val == node_sub.left.val) and
    (not node.right and not node_sub.right or node.right and node_sub.right and node.right.val == node_sub.right.val)
):
                    if all(x is None for x in stack_sub) and not node.left and not node.right and not node_sub.left and not node_sub.right:
                        return True
                    stack_sub.append(node_sub.right)
                    stack_sub.append(node_sub.left)
                else:
                    stack_sub = [subRoot]
                    if res:
                        stack = [res[0]]
                        res.popleft()
                    continue
                stack.append(node.right)
                stack.append(node.left)
        return False
        
      
        

# @lc code=end

