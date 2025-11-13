class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            mn = min(nums)
            idx = nums.index(mn)
            nums[idx] *= multiplier
        return nums