class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: 1}
        cnt = sm = 0
        zero_cnt = 0
        for i, item in enumerate(nums):
            sm += item
            if sm % k in d:
                if item % k == 0:
                    if (sm - item) % k == 0 and i > 0:
                        return True
                    if zero_cnt > 0:
                        return True
                else:
                    return True
            d[sm % k] = d.get(sm % k, 0) + 1
            if item == 0:
                zero_cnt += 1
            else:
                zero_cnt = 0
        return False