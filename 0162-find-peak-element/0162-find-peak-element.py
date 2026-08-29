class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        l,r=0,n-1
        if n==1:
            return 0
        while l<=r:
            mid=l+(r-l)//2
            if mid==n-1 and nums[mid]>nums[mid-1]:
                return mid
            if mid==0 and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid-1
       