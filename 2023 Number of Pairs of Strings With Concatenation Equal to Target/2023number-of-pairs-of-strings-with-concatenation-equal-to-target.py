class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        d = {}
        cnt = 0
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for num in nums:
            result = ''
            if target.startswith(num):
                result = target[len(num):]

            if result and result in d:
                cnt += d[result] if result != num else d[result] - 1  

        return cnt