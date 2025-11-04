class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        cur = first
        for i, item in enumerate(encoded):
            res.append(item ^ cur)
            cur = item ^ cur
        return res