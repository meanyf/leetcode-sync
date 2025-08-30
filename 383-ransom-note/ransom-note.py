class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for item in ransomNote:
            d[item] = d.get(item, 0) + 1
        
        t = {}
        for item in magazine:
            if item in d:
                d[item] -= 1
                if d[item] == 0:
                    del d[item]
        print(d)
        return True if not d else False