#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo = 0
        hi = len(letters) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if letters[mi] <= target:
                lo = mi + 1
            else:
                hi = mi - 1
        if lo >= len(letters):
            return letters[0]
        return letters[lo]
# @lc code=end

