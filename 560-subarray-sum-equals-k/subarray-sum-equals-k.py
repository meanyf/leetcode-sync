
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        sm = cnt = 0
        for item in nums:
            sm += item
            if sm - k in d:
                cnt += d[sm-k] 
            d[sm] = d.get(sm, 0) + 1
        return cnt