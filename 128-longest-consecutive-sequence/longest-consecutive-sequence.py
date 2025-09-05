class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mx = 0
        for num in nums:
            s.discard(num)
            cnt = 1
            cur_num = num + 1
            while cur_num in s:
                s.discard(cur_num)
                cur_num += 1
                cnt += 1
                
            cur_num = num - 1
            while cur_num in s:
                s.discard(cur_num)
                cur_num -= 1
                cnt += 1
            mx = max(mx, cnt)
        return mx