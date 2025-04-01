class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0: 
                if prefix[i] == prefix[len(prefix) - 1] - prefix[i + 1]:
                    cnt += 2
                elif prefix[i] + 1 == prefix[len(prefix) - 1] - prefix[i + 1]:
                    cnt += 1
                elif prefix[i] - 1 == prefix[len(prefix) - 1] - prefix[i + 1]:
                    cnt += 1
        return cnt