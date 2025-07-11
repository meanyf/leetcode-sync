#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        res = []
        for item in lst:
            if item == '..':
                if res:
                    res.pop()
            elif item and item != '.':
                res.append(item)
        print(res)
        return '/' + '/'.join(res)
# @lc code=end