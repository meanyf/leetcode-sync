class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        s1 = set()
        s2 = set()
        for x in paths:
            s1.add(x[0])
            s2.add(x[1]) 
        return list((s2 - s1))[0]
        
