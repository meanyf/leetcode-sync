class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l
        
        def bin_s(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1
        
        l = findMin(nums)
        return max(bin_s(0, l - 1), bin_s(l, len(nums) - 1))
