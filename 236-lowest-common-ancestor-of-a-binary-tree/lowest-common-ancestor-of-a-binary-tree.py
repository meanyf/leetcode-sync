# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        d = {root: None}
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    d[node.right] = node
                    stack.append(node.right)
                if node.left:
                    d[node.left] = node
                    stack.append(node.left)
        cur = p
        st = set()
        while cur:
            st.add(cur)
            cur = d[cur]
        while q not in st:
            q = d[q]
        return q
        
