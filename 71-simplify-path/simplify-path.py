#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        res = ['/']
        for item in lst:
            if res and item == '..':
                if len(res) > 1:
                    res.pop()
            elif item == '.':
                continue
            elif item:
                res.append(item + '/')
        ans = ''.join(res)
        if len(ans) > 1 and ans[-1] == '/':
            return ans[:-1]
        if not ans:
            return '/'
        return ans
# @lc code=end