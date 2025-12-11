class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l, r = math.inf, -math.inf
        left_val, right_val = math.inf, -math.inf
        for i in range(len(nums) -1, 0, -1):
            if nums[i - 1] > nums[i]:
                left_val = min(left_val, nums[i])
                right_val = max(right_val, nums[i - 1])

        if left_val is not None:
            for i in range(len(nums)):
                if left_val < nums[i]:
                    l = min(l, i)
                    break
        
        if right_val is not None:
            for i in range(len(nums) - 1, -1, -1):
                if right_val > nums[i]:
                    r = max(r, i)
                    break

        print(l, r)
        if left_val == math.inf and right_val == -math.inf:
            return 0

        res = r - l + 1
        return res if res != 1 else 0