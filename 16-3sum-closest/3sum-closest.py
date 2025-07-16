class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        min_diff = float('inf')
        n = len(nums)
        
        for idx in range(n - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            l, r = idx + 1, n - 1
            while l < r:
                current_sum = nums[idx] + nums[l] + nums[r]
                current_diff = abs(target - current_sum)
                
                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum
                
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
        return closest_sum