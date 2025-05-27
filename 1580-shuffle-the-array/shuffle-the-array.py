class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [elem for i in range(n) for elem in (nums[i], nums[i + n])]