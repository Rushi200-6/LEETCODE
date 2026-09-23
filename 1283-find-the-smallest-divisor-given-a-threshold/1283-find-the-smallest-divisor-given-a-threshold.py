class Solution(object):
    def smallestDivisor(self, nums, threshold):
        l=1
        r=max(nums)
        ans=r
        while l<=r:
            mid=l+(r-l)//2
            sum=0
            for i in range(0,len(nums)):
                sum+=(nums[i]+mid-1)//mid
            if sum<=threshold:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

        