#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        print(arr)
        l = 0
        r = len(arr) - 1
        cnt = arr.count(0)
        if cnt > 1:
            return True

        while l >= 0 and r >= 0 and l < len(arr) and r < len(arr):
            if l == r and l == len(arr) - 1:
                break
            if arr[l] == arr[r] * 2 or arr[l] * 2 == arr[r]:
                return True

            if l <= r:
                if abs(arr[l] * 2) < abs(arr[r]) and arr[l] != 0 and arr[r] != 0:
                    r -= 1
                else:
                    l += 1
            else:
                if abs(arr[r] * 2) < abs(arr[l]) and arr[l] != 0 and arr[r] != 0:
                    r += 1
                else:
                    l += 1
            print(l, r)

        print(l, r)

        # >>>> Новая мини‑проверка для отрицательных пар:
        for x in arr:
            if x < 0 and 2 * x in arr:
                return True

        return False

