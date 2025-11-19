class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {}
        sm = cnt = 0
        for item in nums:
            d[sm % k] = d.get(sm % k, 0) + 1
            sm += item
            if (sm - k) % k in d:
                cnt += d[(sm - k) % k]
        return cnt
        
