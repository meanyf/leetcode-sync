class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = {}
        sm = 0
        cnt = 0
        for item in nums:
            d[sm] = d.get(sm, 0) + 1
            sm += item % 2
            if sm - k in d:
                cnt += d[sm - k]
        return cnt
            