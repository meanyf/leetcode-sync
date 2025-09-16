class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        while nums and nums[cnt] < k:
            cnt += 1
        return cnt