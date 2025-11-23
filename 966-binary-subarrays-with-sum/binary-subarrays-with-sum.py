class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = sm = 0
        d = {0: 1}
        for item in nums:
            sm += item
            if sm - goal in d:
                cnt += d[sm - goal]
            d[sm] = d.get(sm, 0) + 1
        return cnt