class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if abs(num + 1) % 3 == 0:
                ans += 1
            elif abs(num - 1) % 3 == 0:
                ans += 1
        return ans