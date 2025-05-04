class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = dict()
        for item in dominoes:
            k = ((item[0], item[1]))
            val = ((item[1], item[0]))
            if val in d:
                d[val] = d.get(val, 0) + 1
            else:
                d[k] = d.get(k, 0) + 1
        cnt = 0
        for k in d:
            if d[k] > 1:
                cnt += (d[k] * (d[k] - 1)) // 2
        return cnt