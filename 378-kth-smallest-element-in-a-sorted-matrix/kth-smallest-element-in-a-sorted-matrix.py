class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_and_last_le(x):
            cnt = 0
            last = -float('inf')
            j = n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1
                if j >= 0:
                    cnt += (j + 1)
                    last = max(last, matrix[i][j])
            return cnt, last

        lo, hi = matrix[0][0], matrix[-1][-1]

        while lo < hi:
            mi = (lo + hi) // 2
            cnt, last = count_and_last_le(mi)
            if cnt >= k:
                hi = mi
            else:
                lo = mi + 1
        return lo
