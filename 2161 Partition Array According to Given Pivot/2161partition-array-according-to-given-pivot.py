class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lst = []
        for num in nums:
            if num < pivot:
                lst.append(num)
        for num in nums:
            if num == pivot:
                lst.append(num)
        for num in nums:
            if num > pivot:
                lst.append(num)
        return lst