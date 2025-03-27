class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d1 = {}
        d2 = {}
        lst1 = s1.split()
        lst2 = s2.split()
        for item in lst1:
            d1[item] = d1.get(item, 0) + 1
        for item in lst2:
            d2[item] = d2.get(item, 0) + 1
        res = []
        for k in d1:
            if d1[k] == 1 and k not in d2:
                res.append(k)
        
        for k in d2:
            if d2[k] == 1 and k not in d1:
                res.append(k)
        return res