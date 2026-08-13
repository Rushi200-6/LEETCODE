class Solution:
    def nextPermutation(self, nums):
        n=len(nums)
        pivot=-1
        #find the element that smaller than jusnext number
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        #condition in leetcode
        if pivot==-1:
            nums.reverse()
            return
        #find the next greater number
        for i in range(n-1,pivot,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        #reverse the next remaining part from pivot+1
        i=pivot+1
        j=n-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1