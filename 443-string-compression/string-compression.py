class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 0
        l = r = 0
        res = 0
        while l < len(chars) and r < len(chars):
            res += 1
            cnt = 0
            cur = chars[r]
            while r < len(chars) and cur == chars[r]:
                r += 1
                cnt += 1
            chars[l] = cur
            l += 1
            if cnt != 1:
                size = len(str(cnt))
                for ch in str(cnt):
                    chars[l] = ch
                    res += 1
                    l += 1
        return res