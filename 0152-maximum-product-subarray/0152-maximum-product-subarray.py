class Solution(object):
    def maxProduct(self, nums):
        ans=float('-inf')
        n=len(nums)
        pre=1
        suf=1
        for i in range(0,n):
            if pre==0:
                pre=1
            if suf==0:
                suf=1
            pre=pre*nums[i]

            suf=suf*nums[n-i-1]

            ans=max(ans,max(pre,suf))
        return ans

        