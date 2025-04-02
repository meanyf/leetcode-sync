class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        prefix = [0] * (len(travel) + 1)
        for i in range(1, len(travel) + 1):
            prefix[i] = travel[i - 1] + prefix[i - 1]
        s = ''
        for item in garbage:
            s += item
        s = set(s)
        lst = list(s)
        time = 0
        lastidx = 0
        for i in range(len(s)):
            for j, item in enumerate(garbage):
                if lst[i] in item:
                    time += item.count(lst[i])
                    lastidx = j
            time += prefix[lastidx]
        return time

