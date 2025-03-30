class Solution:
	def returnToBoundaryCount(self, nums: list[int]) -> int:
		arr = [0] * (len(nums) + 1)
		for i in range(1, len(nums) + 1):
			arr[i] = arr[i - 1] + nums[i - 1] 

		cnt = 0
		for num in arr[1:]:
			if num == 0:
				cnt += 1
		return cnt