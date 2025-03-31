class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        prefix_arr = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix_arr[i] = prefix_arr[i - 1] + int(nums[i - 1])
        m = min(prefix_arr)
        return max(1, 1 - m)