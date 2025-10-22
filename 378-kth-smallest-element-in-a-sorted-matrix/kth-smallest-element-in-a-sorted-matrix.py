class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def feasible(x):
            cnt = 0
            last = -float('inf')
            for row in matrix:
                for item in row:
                    if x >= item:
                        cnt += 1
                    if cnt >= k:
                        return cnt
            return cnt
        lo, hi = matrix[0][0], matrix[-1][-1]
        res = None
        while lo < hi:
            mi = (lo + hi) // 2
            res = feasible(mi)
            if res >= k:
                hi = mi
            else:
                lo = mi + 1
        return lo