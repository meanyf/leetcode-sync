# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(a, b):
            stack = [(a, b)]
            while stack:
                x, y = stack.pop()
                if not x and not y:
                    continue
                if not x or not y or x.val != y.val:
                    return False
                stack.append((x.right, y.right))
                stack.append((x.left, y.left))
            return True

        if not subRoot:
            return True
        
        if not root:
            return False
            
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                if node.val == subRoot.val:
                    if check(node, subRoot):
                        return True
        return False