# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('none')
        while res and res[-1] == "none":
            res.pop()
        return ",".join(res)
        # 1, 2, 3; 2, 4, 5; 4, null, null; 5, 6, 7

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return []
        res = data.split(",")
        ans = []
        for item in res:
            if item == "none":
                ans.append(None)
            else:
                ans.append(int(item))
        # res = list(map(int, data.split(',')))

        return ans

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))