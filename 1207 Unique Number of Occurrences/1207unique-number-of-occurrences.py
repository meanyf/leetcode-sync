class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        return len(set(d.values())) == len(d.values())