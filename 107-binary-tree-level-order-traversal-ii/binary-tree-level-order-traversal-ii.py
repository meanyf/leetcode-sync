# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_children(node):
            return [child for child in (node.left, node.right) if child]
        res = []
        def bfs():
            if not root:
                return None
            queue = deque([root])
            while queue:
                level = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    queue.extend(get_children(node))
                res.append(level)
        bfs()
        res.reverse()
        return res