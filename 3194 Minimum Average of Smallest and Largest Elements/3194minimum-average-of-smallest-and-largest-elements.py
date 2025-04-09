class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        res = [0] * (n // 2)
        nums.sort()
        lef = 0 
        r = n - 1
        min_ = (nums[lef] + nums[r]) / 2
        while lef < r:
            res[lef] = (nums[lef] + nums[r]) / 2
            if min_ > res[lef]:
                min_ = res[lef]
            lef += 1
            r -= 1
        return min_