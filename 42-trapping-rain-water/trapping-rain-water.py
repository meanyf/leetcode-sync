#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        def f(height):
            res = 0
            idx = 0
            mx = 0
            l = 0
            while l < len(height):
                if height[l] >= mx:
                    idx = l
                    mx = height[l]
                left = height[l]
                ans = 0
                if left:
                    r = l + 1
                    while r < len(height):
                        right = height[r]
                        if right >= left:
                            res += ans
                            break
                        else:
                            ans += left - height[r]
                        r += 1
                    l = r
                else:
                    l += 1
            return res, len(height) - idx

        ans, idx = f(height)
        res += ans
        new_height = height[::-1]
        new_height = new_height[:idx + 1]
        res += f(new_height)[0]

        return res


# @lc code=end
