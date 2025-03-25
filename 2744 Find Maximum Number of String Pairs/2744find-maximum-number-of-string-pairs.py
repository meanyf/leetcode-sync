class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        d = {}
        cnt = 0
        for item in words:
            if item in d and d[item] > 0:
                cnt += 1
                d[item] -= 1
            d[item[::-1]] = d.get(item[::-1], 0) + 1
        return cnt
        