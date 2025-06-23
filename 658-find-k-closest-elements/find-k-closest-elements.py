from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if arr[mi] < x:
                lo = mi + 1
            else:
                hi = mi
        if lo == len(arr) or (lo == 0 and arr[lo] == x):
            if lo == 0:
                return sorted(arr[:k])
            if lo == len(arr):
                return sorted(arr[-k:])
        l = lo
        if arr[lo] != x and abs(x - arr[lo - 1]) <= abs(x - arr[lo]):
            l -= 1
        r = l + 1
        cnt = 0
        res = deque()
        while cnt < k:
            left = arr[l] if l > -1 else float('inf')
            right = arr[r] if r < len(arr) else float('inf')
            if abs(x - left) <= abs(x - right):
                res.appendleft(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            cnt += 1
        return list(res)