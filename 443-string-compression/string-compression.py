class Solution:
    def compress(self, chars: List[str]) -> int:
        l = r = 0
        while l < len(chars) and r < len(chars):
            cnt = 0
            cur = chars[r]
            while r < len(chars) and cur == chars[r]:
                r += 1
                cnt += 1
            chars[l] = cur
            l += 1
            if cnt != 1:
                for ch in str(cnt):
                    chars[l] = ch
                    l += 1
        return l