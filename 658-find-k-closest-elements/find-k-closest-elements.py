class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        if l == len(arr): 
            l = len(arr) - 1
        res = abs(arr[l] - x)
        if l > 0 and res >= abs(arr[l - 1] - x):
            l -= 1
        r = l + 1
        cnt = 0
        while cnt < k:
            if r >= len(arr):
                l -= 1
            elif l < 0:
                r += 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
            cnt += 1
        return arr[l + 1: r]
            
        