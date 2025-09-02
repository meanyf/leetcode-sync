class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, item in enumerate(nums):
            if item in d:
                if abs(i - d[item]) <= k:
                    return True
            d[item] = i
        return False
