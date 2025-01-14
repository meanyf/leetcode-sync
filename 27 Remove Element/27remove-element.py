class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # temp = None
        # last_idx = len(nums) - 1
        
        # cnt = 0
        # for i in range(len(nums)):
        #     if (nums[i] == val):
        #         cnt += 1

        idx = []
        idx2 = []
        x = False
        cnt = 0
        for i in range(len(nums)):
            if (nums[i] == val):
                cnt += 1 
        for i in range(len(nums) - 1, -1, -1):       
            if (nums[i] == val and x and i < len(nums) - cnt):
                idx.append(i)
            if nums[i] != val:
                    x = True
        
        if not idx:
            for i in range(len(nums)):
                 if nums[i] == val:
                      return i
            

        
        
        
       
        
        cnt = 0
        for i in range(len(nums) -1, -1, -1):

            if (cnt < len(idx) and nums[i] != val):
                cnt += 1
                idx2.append(i)

        # if not idx and not idx2:
        #      if val == nums[0]:
        #         return 1
        #      else:
        #         return 0
        # if idx and not idx2:
        #      return 0
        # if not idx2:
        #      return 1
         

        cnt = 0
        for i in range(len(nums)):
            if (nums[i] == val and cnt < len(idx) and cnt < len(idx2)):

                nums[i] = nums[idx2[cnt]]
                nums[idx2[cnt]] = val     
                cnt = cnt + 1  




        cnt = 0
        for i in range(len(nums)):
            cnt += 1
            if (nums[i] == val):
                 return cnt - 1