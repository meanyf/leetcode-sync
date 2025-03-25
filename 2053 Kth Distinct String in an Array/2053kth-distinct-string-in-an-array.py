class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        d = dict()
        for item in arr:
            d[item] = d.get(item, 0) + 1 
        cnt = 0
        ans = ''
        for item in arr:
            if item in d and d[item] == 1:
                cnt += 1
                if cnt == k:
                    ans = item
        return ans