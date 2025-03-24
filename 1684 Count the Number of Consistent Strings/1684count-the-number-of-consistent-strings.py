class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d = {}
        cnt = 0
        for a in allowed:
            d[a] = True
        for w in words:
            for s in w:
                if s not in d:
                    break
            else:
                cnt += 1
        return cnt