class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        d1 = {}
        d2 = {}
        for item in items1:
            d1[item[0]] = item[1]
        for item in items2:
            d2[item[0]] = item[1]
        lst = []
        for k in d1:
            if k in d2:
                lst.append((k, d1[k] + d2[k]))
            else:
                lst.append((k, d1[k]))
        for k in d2:
            if k not in d1:
                lst.append((k, d2[k]))
        lst = sorted(lst, key=lambda x: x[0])
        return lst