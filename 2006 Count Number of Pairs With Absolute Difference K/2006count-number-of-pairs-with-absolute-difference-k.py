class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        d = {}
        cnt = 0
        # for i in range(len(nums)): 
        #     d[nums[i]] = [nums[i], i]
        # for i in range(len(nums)): 
        #     if nums[i] + k in d and d[nums[i] + k][1]:
        #         cnt += 1
        for num in nums: 
            d[num] = d.get(num, 0) + 1
        for num in nums:
            if num + k in d:
                cnt += d[num + k]

        return cnt 
        return cnt