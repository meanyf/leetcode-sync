class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        hours = [x % 24 for x in hours]
        d = {}
        cnt_12 = 0
        for num in hours:
            if num != 12:
                d[num] = d.get(num, 0) + 1
            else:
                cnt_12 += 1

        cnt = 0
        r = 0
        print(d)
        for num in hours:
            if 24 - num in d and num != 0 and d[24 - num] > 0 and d[num] > 0:
                cnt += d[24 - num] * d[num]    
                d[24 - num] = 0
                d[num] = 0        
            elif num == 0:
                r += 1

        return int(cnt + r * (r - 1) / 2 + cnt_12 * (cnt_12 - 1) / 2)