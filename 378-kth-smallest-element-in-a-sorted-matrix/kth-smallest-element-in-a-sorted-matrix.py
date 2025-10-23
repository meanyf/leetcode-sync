class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def feasible(x):
            cnt = 0
            j = len(matrix) - 1
            last = -float('inf')
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1
                cnt += j + 1
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