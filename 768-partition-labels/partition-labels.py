#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, ch in enumerate(s):
            d[ch] = i
        mx = 0
        res = []
        prev = 0
        for i, ch in enumerate(s):
            mx = max(mx, d[ch])
            if mx == i:
                res.append(d[ch] + 1 - prev)
                prev += res[-1]
        return res
# @lc code=end

