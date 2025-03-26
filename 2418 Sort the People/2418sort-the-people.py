class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        d = {}
        for i in range(len(heights)):
            d[heights[i]] = names[i]
        
        lst = sorted(d, reverse=True)
        return [d[x] for x in lst]