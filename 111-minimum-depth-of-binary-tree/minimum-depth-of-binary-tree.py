# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        mn = float('inf')
        depth = 1
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    mn = min(mn, depth)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue.extend(level)
            depth += 1
        return mn
        # if not root:
        #     return 0
        # mn = float('inf')
        # def dfs(node, depth):
        #     nonlocal mn
        #     if not node:
        #         return 0
        #     if not node.left and not node.right:
        #         mn = min(mn, depth)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        # dfs(root, 1)
        # return mn