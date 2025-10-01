class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums) - 1
        cnt = 0
        while lo <= hi:
            mi = (lo + hi) // 2
            cnt = 0
            for item in nums:
                if item <= mi:
                    cnt += 1
            if cnt > mi:
                hi = mi - 1
            else:
                lo = mi + 1 
        return lo

        