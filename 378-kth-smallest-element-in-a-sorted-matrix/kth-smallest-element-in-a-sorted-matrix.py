class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def feasible(x):
            cnt = 0
            last = -float('inf')
            for row in matrix:
                for item in row:
                    if x >= item:
                        cnt += 1
                        last = max(last, item)
                    if cnt > k:
                        return False, cnt
            if cnt == k:
                return True, last
            return False, cnt
        lo, hi = matrix[0][0], matrix[-1][-1]
        res = None
        while lo <= hi:
            mi = (lo + hi) // 2
            b, res = feasible(mi)
            if b:
                return res
            if res > k:
                hi = mi - 1
            else:
                lo = mi + 1
        print(mi)
        return lo
