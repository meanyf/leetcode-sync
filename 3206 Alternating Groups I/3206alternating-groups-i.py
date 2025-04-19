class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        lst1 = [1, 0, 1]
        lst2 = [0, 1, 0]
        res = 0
        colors += [colors[0]] + [colors[1]]
        n = len(colors)
        if colors[0:3] == lst1 or colors[0:3] == lst2:
            res += 1
        l = 1
        r = 3
        while r < n:
            if colors[l:r + 1] == lst1 or colors[l:r + 1] == lst2:
                res += 1
            l += 1
            r += 1
            
        return res