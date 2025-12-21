class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for item in nums:
            d[item] = d.get(item, 0) + 1
        
        res = [(key, val) for key, val in d.items()]
        res.sort(key=lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(res[i][0])
        return ans