class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums) - 1
        lst = []
        while l <= r:
            if (nums[r]**2 >= nums[l]**2):
                lst.append(nums[r]**2)
                r -= 1
            else:
                lst.append(nums[l]**2)
                l += 1
        print(lst)
        lst.reverse()
        return lst