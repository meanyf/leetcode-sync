class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        res = []
        l, r = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            prev_l, prev_r = l, r
            l = max(l, intervals[i][0])
            r = min(r, intervals[i][1])
            if l > r:
                res.append([prev_l, prev_r])
                l, r = intervals[i][0], intervals[i][1]
            else:
                l = min(prev_l, intervals[i][0])
                r = max(prev_r, intervals[i][1])
        res.append([l, r])
        return res