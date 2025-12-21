class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)

        # --- обработка начала ---
        l = 0
        while l < n and seats[l] == 0:
            l += 1
        
        # если нет ни одной 1 (теоретически)
        if l == n:
            return n - 1
        
        res = l  # расстояние до первой единицы, если она не в начале
        r = l + 1

        # --- основной цикл между единицами ---
        while r < n:
            if seats[r] == 1:
                res = max(res, (r - l) // 2)
                l = r
            r += 1

        # --- обработка конца ---
        res = max(res, n - 1 - l)

        return res
