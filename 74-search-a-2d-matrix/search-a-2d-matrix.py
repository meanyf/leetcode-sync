class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            first, last = matrix[mi][0], matrix[mi][-1]
            if target < first:
                hi = mi - 1
            elif last < target:
                lo = mi + 1
            else:
                row = mi
                lo, hi = 0, len(matrix[0]) - 1
                while lo <= hi:
                    mi = (lo + hi) // 2
                    if matrix[row][mi] == target:
                        return True
                    if matrix[row][mi] < target:
                        lo = mi + 1
                    else:
                        hi = mi - 1
                return False
        return False

