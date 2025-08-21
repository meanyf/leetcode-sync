from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def find_max_subarray(arr, left, right):
            # Базовый случай: если в подмассиве только один элемент.
            if left == right:
                return arr[left]
            
            mid = (left + right) // 2
            
            # 1. Максимальная сумма в левой половине.
            max_left = find_max_subarray(arr, left, mid)
            
            # 2. Максимальная сумма в правой половине.
            max_right = find_max_subarray(arr, mid + 1, right)
            
            # 3. Максимальная сумма подмассива, пересекающего середину.
            max_cross = self.find_max_crossing_subarray(arr, left, mid, right)
            
            return max(max_left, max_right, max_cross)

        return find_max_subarray(nums, 0, len(nums) - 1)

    def find_max_crossing_subarray(self, arr, left, mid, right):
        # Находим максимальную сумму, начиная от середины и идя влево.
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += arr[i]
            if current_sum > left_sum:
                left_sum = current_sum
        
        # Находим максимальную сумму, начиная от середины + 1 и идя вправо.
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += arr[i]
            if current_sum > right_sum:
                right_sum = current_sum
                
        return left_sum + right_sum