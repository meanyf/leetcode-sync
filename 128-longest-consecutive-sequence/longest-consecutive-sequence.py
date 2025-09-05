class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mx = 0
        for num in s:
            if num - 1 not in s:
                cnt = 0
                cur_num = num
                while cur_num in s:
                    cur_num += 1
                    cnt += 1
                mx = max(mx, cnt)
        return mx