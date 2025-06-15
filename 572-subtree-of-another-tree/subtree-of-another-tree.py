# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: 'TreeNode', subRoot: 'TreeNode') -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def isSameTree(p: 'TreeNode', q: 'TreeNode') -> bool:
            stack_p = [p]
            stack_q = [q]
            
            while stack_p and stack_q:
                node_p = stack_p.pop()
                node_q = stack_q.pop()
                
                if not node_p and not node_q:
                    continue
                if not node_p or not node_q:
                    return False
                if node_p.val != node_q.val:
                    return False
                
                stack_p.append(node_p.right)
                stack_p.append(node_p.left)
                stack_q.append(node_q.right)
                stack_q.append(node_q.left)
            
            return not stack_p and not stack_q
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return False
