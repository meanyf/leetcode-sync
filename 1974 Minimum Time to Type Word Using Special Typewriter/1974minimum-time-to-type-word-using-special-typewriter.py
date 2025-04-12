class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 1
        dif = abs(ord('a') - ord(word[0]))
        ans += min(dif, 26 - dif)
        for idx, ch in enumerate(word):
            if idx > 0:
                dif = abs(ord(word[idx]) - ord(word[idx - 1]))
                ans += min(dif, 26 - dif) + 1
        return ans