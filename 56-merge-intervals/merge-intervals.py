class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        res = []
        l, r = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start > r:
                res.append([l, r])
                l, r = start, end
            else:
                l = min(l, start)
                r = max(r, end)
        res.append([l, r])
        return res