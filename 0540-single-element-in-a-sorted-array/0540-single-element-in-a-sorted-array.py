class Solution(object):
    def singleNonDuplicate(self, nums):
        n=len(nums)
        l,r=0,n-1
        if n==1:
            return nums[0]
        while l<=r:
            mid=l+(r-l)//2
            if mid==0 and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid==n-1 and nums[mid]!=nums[mid-1]:
                return nums[mid]
            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            if mid % 2==0:
                if nums[mid]==nums[mid-1]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]==nums[mid-1]:
                    l=mid+1
                else:
                    r=mid-1
            