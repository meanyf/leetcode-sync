#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        def f():
            res = 0
            l = 0
            while l < len(height):
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
            return res
        res += f()
        max_value = max(height)
        idx = max(i for i, x in enumerate(height) if x == max_value)
        print(idx) # 0
        # 1 3 4 2
        idx = len(height) - idx
        # 2 4 3 1
        height.reverse()
        height = height[:idx + 1]
        print(height)
        res += f()

        return res
# @lc code=end
