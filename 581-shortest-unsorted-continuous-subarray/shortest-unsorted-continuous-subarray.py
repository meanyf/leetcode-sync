class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = 0, -1
        left_val, right_val = math.inf, -math.inf
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                left_val = min(left_val, nums[i])
                right_val = max(right_val, nums[i - 1])

        for i in range(len(nums)):
            if left_val < nums[i]:
                l = i
                break
        
        for i in range(len(nums) - 1, -1, -1):
            if right_val > nums[i]:
                r = i
                break

        return r - l + 1