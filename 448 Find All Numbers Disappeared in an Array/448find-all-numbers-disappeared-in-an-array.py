class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
         for num in nums:
            index = abs(num) - 1  # Находим индекс, соответствующий числу
            if nums[index] > 0:
                nums[index] = -nums[index]
         print(nums)