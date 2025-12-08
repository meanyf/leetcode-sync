class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = math.inf
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < target:
                    left_val = nums[l]
                    while l < r and left_val == nums[l]:
                        l += 1
                elif total > target:
                    right_val = nums[r]
                    while l < r and right_val == nums[r]:
                        r -= 1
                else:
                    return target
                if abs(target - total) < abs(target - res):
                    res = total
        return res