#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = nums[0]
        insert = 1
        for i in range(1, len(nums)):
            if prev != nums[i]:
                nums[insert] = nums[i]
                insert += 1
            prev = nums[i]
        return insert
# @lc code=end

