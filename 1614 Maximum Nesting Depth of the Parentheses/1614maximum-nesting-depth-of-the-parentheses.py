class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        mx = 0
        for ch in s:
            if ch == '(':
                cnt += 1
            if ch == ')':
                cnt -= 1
            mx = max(cnt, mx)
        return mx