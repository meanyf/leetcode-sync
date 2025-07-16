class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i,v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                val = v + nums[l] + nums[r]

                if val == 0:
                    res.append([nums[l], nums[r], v])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                elif val < 0:
                    l += 1
                else:
                    r -= 1
        return res