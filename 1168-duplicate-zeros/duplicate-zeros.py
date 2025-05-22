#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        i = 0
        while i < len(arr) - idx:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                idx += 1
                i += 1
            i += 1
        print(arr)
        for i in range(idx):
            arr.pop()
        

# @lc code=end

