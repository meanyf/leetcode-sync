class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_num = 0
        uniq = []
        if len(nums) == 0:
            return 0
        else:
            first_num = nums[0]   
            uniq.append(first_num)

        for i, num in enumerate(nums):
            if num != first_num:
                first_num = num
                uniq.append(num)

        uniq_l = len(uniq)        
        uniq_counter = 0
        for i, num in enumerate(nums):
            if i < uniq_l:
                nums[i] = uniq[uniq_counter]
                uniq_counter += 1
        return uniq_l