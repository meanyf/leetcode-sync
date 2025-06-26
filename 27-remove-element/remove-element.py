#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap = len(nums) - 1
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[swap] = nums[swap], nums[i]
                swap -= 1
                cnt += 1
        return len(nums) - cnt
# @lc code=end

