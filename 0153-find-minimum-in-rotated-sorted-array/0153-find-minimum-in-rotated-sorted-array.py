class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        mini=("-inf")
        l,h=0,n-1
        while l<=h:
            mid=l+(h-l)//2
            if nums[mid]<=nums[h]:
                mini=min(mini,nums[mid])
                h=mid-1
            else:
                mini=min(mini,nums[l])
                l=mid+1
        return mini
        