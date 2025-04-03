class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        pref_n = n // 2
        print(pref_n)
        prefev = [0] * (n + 1)
        prefodd = [0] * (n + 1)

        for i in range(1, n + 1):
            if (i - 1) % 2 == 0:
                prefev[i] = prefev[i - 1] + nums[i - 1]
                prefodd[i] = prefodd[i - 1]
            else:
                prefodd[i] = prefodd[i - 1] + nums[i - 1]
                prefev[i] = prefev[i - 1]
        cnt = 0
        for i in range(n):
            even_sum = prefev[i] + (prefodd[n] - prefodd[i + 1])
            odd_sum = prefodd[i] + (prefev[n] - prefev[i + 1])
            cnt += 1 if even_sum == odd_sum else 0 
        
        print(prefev)
        print(prefodd)
        return cnt 

        
