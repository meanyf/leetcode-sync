class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 10**6
        for i in range  (len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total - target < 0:
                    l += 1
                elif total - target > 0:
                    r -= 1
                else:
                    return target
                if abs(target - total) < abs(target - res):
                    res = total
        return res