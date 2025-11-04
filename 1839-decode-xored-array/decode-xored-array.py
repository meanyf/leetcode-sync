class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        prev = first
        res = [prev]
        for i, item in enumerate(encoded):
            prev = item ^ prev
            res.append(prev)
        return res