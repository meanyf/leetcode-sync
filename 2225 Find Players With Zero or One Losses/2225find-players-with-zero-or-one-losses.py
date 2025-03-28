class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        d = {}
        s1 = set()
        s2 = set()
        for item in matches:
            d[item[1]] = d.get(item[1], 0) + 1
            s1.add(item[0])
            s2.add(item[1])
        lst = [x[0] for x in list(d.items()) if x[1] == 1]
        return (sorted(s1 - s2), sorted(lst))
