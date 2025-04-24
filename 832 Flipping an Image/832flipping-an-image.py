#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        def reverse(nums: list, n):
            for i in range(n//2):
                nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]
        def invert(nums, n):
            for i in range(n):
                nums[i] = int(not nums[i])
        cols = len(image[0])
        for row in image:
            reverse(row, cols)
            invert(row, cols)
        return image
# @lc code=end

