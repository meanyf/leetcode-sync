class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        sm = 0
        for i, item in enumerate(nums):
            sm += item
            if sm % k in d:
                if i - d[sm % k] > 1:
                    return True
            else:
                d[sm % k] = i
        return False