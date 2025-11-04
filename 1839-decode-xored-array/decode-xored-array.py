class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        prev = first
        res = [prev]
        for i, item in enumerate(encoded):
            res.append(item ^ prev)
            prev = item ^ prev
        return res