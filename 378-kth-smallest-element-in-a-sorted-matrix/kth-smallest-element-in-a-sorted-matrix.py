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
        ans = None
        while lo <= hi:
            mi = (lo + hi) // 2
            if feasible(mi) >= k:
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans