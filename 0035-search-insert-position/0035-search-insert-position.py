class Solution(object):
    def searchInsert(self, nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l+=1
            else:
                r-=1
        return l
    
#two pointers using binary search