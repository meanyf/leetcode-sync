class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.right and root.left.val != root.right.val:
            return False
        stack = [(root.left, root.right)]
        while stack:
            left_root, right_root = stack.pop()
            if left_root and right_root:
                if left_root.val != right_root.val:
                    return False
            elif left_root:
                return False
            elif right_root:
                return False
            if left_root or right_root:
                stack.append((left_root.right if left_root else None, right_root.left if right_root else None))
                stack.append((left_root.left if left_root else None, right_root.right if right_root else None))
        return True
            
