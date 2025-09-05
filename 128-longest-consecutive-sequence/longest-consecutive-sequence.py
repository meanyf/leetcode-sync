class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mx = 0
        for num in nums:
            cnt = 0
            if num - 1 not in s:
                cur_num = num
                while cur_num in s:
                    s.discard(cur_num)
                    cur_num += 1
                    cnt += 1
                mx = max(mx, cnt)
        return mx