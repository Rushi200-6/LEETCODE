class Solution:
    def maxSubArray(self, nums):
        
        # current_sum = nums[0]
        # max_sum = nums[0]

        # for num in nums[1:]:
            
        #     current_sum = max(num, current_sum + num)
        #     max_sum = max(max_sum, current_sum)

        # return max_sum


        n=len(nums)
        maxi=float('-inf')
        total=0
        for i in range(0,n):
            total+=nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi