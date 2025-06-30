#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        if not intervals:
            return []
        current = intervals[0]
        for i in range(1, len(intervals)):
            item = intervals[i]
            if item[0] <= current[1] <= item[1] or current[0] <= item[0] <= current[1]:
                current[0] = min(current[0], item[0])
                current[1] = max(current[1], item[1])
            else:
                res.append(current)
                current = item
        if current:
            res.append(current)
        return res

        
        
        
        
        
        
        
        
        
        
        
        
        
        # lst = []
        # length = len(intervals)
        # # for i in range(len(intervals)):

        # left = 0
        # res = []
        # while left < length - 1:
        #     if intervals[left + 1][0] <= intervals[left][1] <= intervals[left + 1][1]:
        #         res = [intervals[left + 1][0], intervals[left + 1][1]]
        #     else:
        #         if res:
        #             lst.append(res)
                
# @lc code=end

