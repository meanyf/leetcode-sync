# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root, subRoot):
            stack = [(root, subRoot)]
            while stack:
                first_node, snd_node = stack.pop()
                if first_node is not None and snd_node is None:
                    return False
                if first_node is None and snd_node is not None:
                    return False
                if first_node is not None and snd_node is not None:
                    if first_node.val != snd_node.val:
                        return False
                    stack.append((first_node.right, snd_node.right))
                    stack.append((first_node.left, snd_node.left))
            return True

        if not root and not subRoot:
            return True
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