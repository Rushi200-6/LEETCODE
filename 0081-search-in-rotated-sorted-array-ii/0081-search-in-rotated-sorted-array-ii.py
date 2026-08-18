class Solution:
    def search(self, nums, target):
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return True
            if nums[l]==nums[mid]==nums[r]:
                l+=1
                r-=1
                continue
            if nums[mid]<=nums[r]:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[l]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return False
                
#similar to search in sorted array 1 but 1 extra additional condition required to handle the duplicates 