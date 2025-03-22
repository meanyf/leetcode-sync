class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        s = set()
        print(nums)
        while left < right:
            s.add((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return len(s)
