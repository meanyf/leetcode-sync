class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        arr1 = [0] * len(nums)
        arr2 = [0] * len(nums)
        for i in range(0, len(arr1)):
            arr1[i] = len(set(nums[0:i + 1]))
        for i in range(0, len(arr2)):
            arr2[i] = len(set(nums[i + 1:]))
        diff = [0] * len(nums)
        for i in range(len(nums)):
            diff[i] = arr1[i] - arr2[i]
        return diff