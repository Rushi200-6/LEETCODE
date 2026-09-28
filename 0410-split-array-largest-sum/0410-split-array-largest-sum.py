class Solution(object):
    def splitArray(self, nums, k):
        n=len(nums)
        def ispossible(nums,mid,k):
            p,t=1,0
            for i in range(0,n):
                if t+nums[i]<=mid:
                    t+=nums[i]
                else:
                    p+=1
                    t=nums[i]
            return p<=k

        l,r=max(nums),sum(nums)
        ans=-1
        while l<=r:
            mid=l+(r-l)//2
            if ispossible(nums,mid,k):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
            

        