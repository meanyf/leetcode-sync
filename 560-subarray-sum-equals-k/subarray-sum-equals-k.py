class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        sm = 0
        cnt = 0
        for item in nums:
            d[sm] = d.get(sm, 0) + 1
            sm += item
            if sm - k in d:
                cnt += d[sm - k]
        return cnt