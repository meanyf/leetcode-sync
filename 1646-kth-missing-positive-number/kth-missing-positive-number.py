#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 0
        idx = 0
        for i in range(1, arr[len(arr) - 1] + 1 + k + 1):
            if idx < len(arr) and i == arr[idx]:
                idx += 1
            else:
                cnt += 1
            if cnt == k:
                return i
# @lc code=end

