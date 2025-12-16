# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        stack_left = [root.left]
        stack_right = [root.right]
        while stack_left and stack_right:
            left = stack_left.pop()
            right = stack_right.pop()
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False
            if left and right:
                if left.val != right.val:
                    return False
                stack_left.append(left.right)
                stack_left.append(left.left)
                
                stack_right.append(right.left)
                stack_right.append(right.right)
        return True