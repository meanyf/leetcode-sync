class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        st = set(friends)
        res = []
        for item in order:
            if item in st:
                res.append(item)
        return res