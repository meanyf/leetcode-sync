class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        cnt = 0
        length = len(nums)
        s = set()
        for num in nums:
            s.add(num)
        for i in range(length):
            if nums[i] + diff in s and nums[i] + 2 * diff in s:
                cnt += 1
        return cnt